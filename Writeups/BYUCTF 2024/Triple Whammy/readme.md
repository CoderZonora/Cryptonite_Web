<h1> Triple whammy - web </h1>

Note: 
For all web challenges, for reasons unknown to mankind, 
calls back to webhook.site(and perhaps others) are not working
so try to use something like https://requestcatcher.com/ (which is confirmed to work)

Maybe because this was hosted on AWS and its firewall was blocking requests from certain sites as they might be spammmy.
</blockquote>

<p> In this challenge they gave us source code of the server and admin bot source code </p>

As we can see there is XSS vector on this line in server.py ` return 'Nope still no front end, front end is for noobs '+name`
Another endpoint is `/query` where we can see if cookie is matching the secret it takes `url` parameter which is being parsed and
there is a check that url has to have scheme of `http` or `https` and that hostname is `127.0.0.1`- on valid url server will make a request to it. 
Which concludes that this will be *SSRF*  with local service in play. There was yet another file called internal.py which we were supposed to bypass to get the flag.

There are two things here:
  - Port is random
  - Unsafe usage of pickle which we will utilize for RCE
   

## Solution

Below is the full script, which will send malicious link to the bot to trigger XSS that will further make a request to `/query` and we know that cookie check is done on that endpoint so we need bot to make a request with its cookie.
From `admin_bot.js` bot was setting cookie with `httpOnly: true` but that doesn't matter since we are not trying to extract nor access the bot's cookie with JS. Bot will send its cookie by default which is only thing that we care about for this to successfully make a request to the servers `/query` endpoint.
The RCE payload will `cat flag.txt` and pass the data to our server that we control via `curl` request.
Since range of 300 random ports is not much, it was just bruteforceable.
 

On correct bruteforce received request was:

` GET /q?data=byuctf%7Byou_got_a_turkey%21%21%21%7D HTTP/1.1`

<b> FLAG: byuctf{you_got_a_turkey!!!}</b>
