# XS - Leaks Report

XS-Leaks is a WebEx method infer the information using side-channel attacks like timing attacks rather than directly accessing any data. 
Most of the time it can be prevented by having the correct same origin and cross origin settings.
But this attack vector is not always very reliable as some attacks might break due to a variety of external factors like DNS load times, network congestion etc.
 
#### What is eTLD and TLD+1?

Top level domains (TLD) are listed here: https://www.iana.org/domains/root/db. TLD + 1 basically means the combination
of TLD and the part of the domain just before it, irrespective of the number of subdomain levels the domain has. 

TIL about the [Public Suffix List](https://publicsuffix.org/learn/).
[Better Explanation](https://devcenter.heroku.com/articles/cookies-and-herokuapp-com)
Now for domains of the form `.co.in` this won't work and so there is another separate list of eTLD's.

Note: HTTP headers Sec-\* cannot be modified by Javascript in the browser directly. It is one of the forbidden requests headers.
https://fetch.spec.whatwg.org/#forbidden-request-header

Ref : Lots of possible challenge ideas possible based on [this](https://cheatsheetseries.owasp.org/cheatsheets/XS_Leaks_Cheat_Sheet.html) article, implementation is a different issue.


## Same site and Same Origin

Ref: [web.dev](https://web.dev/articles/same-site-same-origin) 

Same-origin is more strict than same site. It also becomes same-origin when the entire combination of scheme,hostname and 
port are same, even different subdomains or different port nnumber on same domain will be considered cross-origin.

On the other hand requests are considered same-site if they have the same eTLD+1 and same scheme.

Major types of Sec-headers:

`sec-fetch-site`: This can be none, cross-site, same-site, same-origin. Its none when the request is created by a user originated action for example : Entering a URL into the address bar

`sec-fetch-dest`: This headers defines what is the final destination of the request and thus it may be denied if it is loaded in an iframe for example.

`sec-fetch-user`: If request is created by user-originated action it is `?1` else the header is not present.

`sec-fetch-mode`: This allows a server to distinguish between requests originating from a user navigating between HTML pages, and requests to load images and other resources.
 For example, this header would contain `navigate` for top level navigation requests, while `no-cors` is used for loading an image.

### Types of xs-leaks side channel:

- iframe counting: If we have an action which if successful executes we can get an iframe to open and if its not succesful it does not, we can count the umber of iframes get opened to infer some data like 
how many records matched a search.

- Cache Probing: Depending on time taken to load certain elements we can infer knowledge about the state of the user. 

- Based on events
	Things like response code, onload and onerror events can help us know about the access a user may have, info about them etc.
	Eg: If we have a query param like ?query=admin and it returns a 200 response code or 404 can tell us about level of access of the user and does
	it trigger an onload event or onerror event.
	
- Postmessage broadcasts: If target origin is a \* wildcard other origins can also receive the message and might get sensetive info not intended for them.

- Focus elements based on URL fragements:  Sometimes applications can use sensetive info as an id of an element on the page and we can use url fragments (https://example.com#sensitive-id) to brute force 
the data depending on weather focus and blur events get fired ot not. 

- [Many others](https://xsleaks.dev/docs/attacks/element-leaks/)

Need to read more into this and solve its chals and read writeups. 
Till now only majorly only referred to [this](https://blog.huli.tw/2022/06/14/en/justctf-2022-xsleak-writeup/) one. 
