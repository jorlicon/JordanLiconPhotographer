import fs from "node:fs";

const blogPath = "blog.html";
const homepagePath = "index.html";
const blogHtml = fs.readFileSync(blogPath, "utf8");
const homepageHtml = fs.readFileSync(homepagePath, "utf8");

function firstMatch(pattern, source, label) {
  const match = source.match(pattern);
  if (!match) throw new Error(`Could not read ${label} from blog.html`);
  return match[1].trim();
}

function escapeHtml(value) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

const posts = [...blogHtml.matchAll(/<article class="post-card">([\s\S]*?)<\/article>/g)].map((match) => {
  const block = match[1];
  const date = firstMatch(/class="post-meta mono">([^<]+)</, block, "post date");
  const title = firstMatch(/<h2>([\s\S]*?)<\/h2>/, block, "post title");
  const description = firstMatch(/<p>([\s\S]*?)<\/p>/, block, "post description");
  const href = firstMatch(/<a class="post-link mono" href="([^"]+)"/, block, "post link");
  const parsedDate = Date.parse(date.replace(/\s+-\s+\d+\s+min read$/i, ""));
  if (Number.isNaN(parsedDate)) throw new Error(`Could not parse post date: ${date}`);
  if (!href.startsWith("post/")) throw new Error(`Unexpected post link: ${href}`);
  return { date, title, description, href, parsedDate };
}).sort((a, b) => b.parsedDate - a.parsedDate);

if (posts.length < 4) throw new Error(`Expected at least four blog posts, found ${posts.length}`);

const cards = posts.slice(0, 4).map((post) => [
  "<article class=\"blog-card\">",
  `<div class=\"blog-meta mono\">${escapeHtml(post.date)}</div>`,
  `<h3>${escapeHtml(post.title)}</h3>`,
  `<p>${escapeHtml(post.description)}</p>`,
  `<a href=\"${escapeHtml(post.href)}\" class=\"blog-link mono\">Read Article</a>`,
  "</article>",
].join(""));

// Keep the cards in static HTML so search engines and visitors get the same content without JavaScript.
const sectionPattern = /(<section[^>]*id="blog"[^>]*>[\s\S]*?<div class="blog-grid">)([\s\S]*?)(<\/div><\/div><\/section>)/;
if (!sectionPattern.test(homepageHtml)) throw new Error("Could not find the homepage blog section");

const generated = [
  "<!-- HOMEPAGE_LATEST_BLOG_START -->",
  cards.join(""),
  "<!-- HOMEPAGE_LATEST_BLOG_END -->",
].join("");
const updatedHomepage = homepageHtml.replace(sectionPattern, `$1${generated}$3`);
fs.writeFileSync(homepagePath, updatedHomepage);

console.log(`Updated homepage with: ${posts.slice(0, 4).map((post) => post.title).join(" | ")}`);
