import { Config } from "@remotion/cli/config";

// Point at a system-installed headless Chromium instead of letting Remotion
// download its own on first render. Useful in sandboxed/offline CI
// environments where Remotion's own browser-download host is blocked; set
// REMOTION_BROWSER_EXECUTABLE to override, otherwise Remotion downloads its
// own browser as normal (the default, recommended path for a real machine).
const browserExecutable = process.env.REMOTION_BROWSER_EXECUTABLE;
if (browserExecutable) {
  Config.setBrowserExecutable(browserExecutable);
}
