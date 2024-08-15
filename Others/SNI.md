Based on CTFZone 2024 - Youtube Unblocker
SNI - Server Name Identification and SNI Spoofing

In HTTPS, a TLS handshake takes place first, before the HTTP conversation can begin (HTTPS still uses HTTP – it just encrypts the HTTP messages). 
For web servers which handle multiple domains under one IP this creates a problem becasue each hostname has its own SSL certificate.
A solution for running several HTTPS servers on a single IP address is TLS Server Name Indication extension (SNI, RFC 6066),
which allows a browser to pass a requested server name during the SSL handshake. 
Without SNI, then, there is no way for the client to indicate to the server which hostname they're talking to.
SNI is currently supported by all modern browsers,though may not be used by some old or special clients.

SNI also prevents what's known as a "common name mismatch error": when a client (user) device reaches the right IP address for a website, 
but the name on the SSL certificate doesn't match the name of the website. 
Often this kind of error results in a "Your connection is not private" error message in the user's browser.
This is because if the server_name is not correctly received the server provides the default certificate which does not match the certificate 
of the requested host.

Whitepaper notes:(SNI Spoofing)
But SNI is also used by ISP's to filter traffic.You see ISP's in certain places give content specific plans. Like a meet plan which has discounted 
data rates for certain services like google meet,zoom etc with whom they have a tie up. 
So if you use these services you're charged a different rate than when you browse the internet normally.
Now with the adoption of HTTPS deep packet inspection has been made difficult.So ISP's use other techniques one of which is SNI identification.
So what some people do is spoof their SNI to point towards the hostname which qualify for the lower data rates while actually accessing other content.
This can be done with the help of self signed certificates and a VPS in the middle which routes the traffic to the actual destination.
SNI proxy service: https://github.com/Intika-Linux-Proxy/SNI-SSL-Proxy
Ref:
https://medium.com/@hirushaadi/tcp-over-ssl-tunnel-with-sni-spoofing-analysis-da7f267bad56

https://en.wikipedia.org/wiki/Server_Name_Indication

https://nginx.org/en/docs/http/configuring_https_servers.html#sni

https://synthical.com/article/Contournement-des-packages-Internet-bas%C3%A9s-sur-le-contenu-avec-un-tunnel-SSL-%2F-TLS%2C-l%27usurpation-SNI-et-l%27usurpation-DNS-834c58d2-ffac-11ed-9b54-72eb57fa10b3



