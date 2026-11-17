const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const root = path.resolve(process.argv[2] || process.cwd());

function scriptFrom(html) {
  const marker = '<script data-jlp-conversion-tracking>';
  const start = html.indexOf(marker);
  assert.notEqual(start, -1);
  return { code: html.slice(start + marker.length, html.indexOf('</script>', start)), start };
}

function run(html, pathname, storage = new Map(), blocked = false, readyState = 'loading') {
  const script = scriptFrom(html);
  const listeners = {};
  const ready = [];
  const form = {
    id: '', dataset: {},
    getAttribute: () => '',
    querySelector: () => null,
    addEventListener: (name, fn) => { listeners[name] = fn; }
  };
  let parsed = readyState !== 'loading' || html.indexOf('<form') < script.start;
  const document = {
    readyState, title: 'Corporate Team Headshots', referrer: '',
    querySelectorAll: selector => selector === 'form' && parsed && html.includes('<form') ? [form] : [],
    addEventListener: (name, fn) => { if (name === 'DOMContentLoaded') ready.push(fn); }
  };
  const sessionStorage = {
    getItem: key => { if (blocked) throw Error('Storage blocked'); return storage.get(key) || null; },
    setItem: (key, value) => { if (blocked) throw Error('Storage blocked'); storage.set(key, value); },
    removeItem: key => { if (blocked) throw Error('Storage blocked'); storage.delete(key); }
  };
  const context = { document, location: { pathname, search: '' }, sessionStorage, URLSearchParams };
  context.window = context;
  vm.runInNewContext(script.code, context);
  parsed = true;
  document.readyState = 'interactive';
  ready.forEach(fn => fn());
  return { listeners, events: () => Array.from(context.dataLayer || [], args => args[1]) };
}

if (process.argv[3]) {
  const original = fs.readFileSync(process.argv[3], 'utf8');
  assert.equal(run(original, '/corporate-team-headshots-el-paso.html').listeners.submit, undefined);
  console.log('Confirmed original corporate form has no submission listener at parse time.');
}

const candidate = fs.readFileSync(path.join(root, 'corporate-team-headshots-el-paso.html'), 'utf8');
const success = fs.readFileSync(path.join(root, 'success.html'), 'utf8');
assert.ok(candidate.indexOf('</form>') < candidate.indexOf('</body>'));
const storage = new Map();
const corporate = run(candidate, '/corporate-team-headshots-el-paso.html', storage);
assert.equal(typeof corporate.listeners.submit, 'function');
assert.equal(typeof run(candidate, '/corporate-team-headshots-el-paso.html', new Map(), false, 'complete').listeners.submit, 'function');
corporate.listeners.submit();
assert.deepEqual(corporate.events(), ['jlp_form_submit', 'submit_project_inquiry']);
assert.equal(JSON.parse(storage.get('jlp_lead_context')).form_name, 'project-inquiry');
assert.equal(run(success, '/success.html', storage).events().filter(e => e === 'generate_lead').length, 1);
assert.equal(run(success, '/success.html', storage).events().length, 0);
assert.equal(run(success, '/success.html').events().length, 0);
const blocked = run(candidate, '/corporate-team-headshots-el-paso.html', new Map(), true);
assert.doesNotThrow(() => blocked.listeners.submit());
assert.equal(blocked.events().includes('jlp_form_submit'), true);
const homeStorage = new Map();
const home = run(fs.readFileSync(path.join(root, 'index.html'), 'utf8'), '/', homeStorage);
home.listeners.submit();
assert.equal(home.events().includes('generate_lead'), false);
assert.equal(run(success, '/success.html', homeStorage).events().filter(e => e === 'generate_lead').length, 1);
assert.equal(run(success, '/success.html', homeStorage).events().length, 0);
console.log('PASS: corporate/home handoff, success once, direct/refresh zero, blocked storage.');
