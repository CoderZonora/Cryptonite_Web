<h1>Anti inspect </h1>
The webpage has a heavy javascript function which overloads the browser by having infinite loop
causing it to crack. Just using command-line curl to GET the webpage reveals the flag.


<h1> Traversed </h1>

Simple path traversal with url encoded request.
So `{url}/..%2Fflag.txt`

<h1>jwt-1</h1>
Use jwt.io to decode a jwt token. Change admin to true. 
The vuln is that the server is not checking if the secret matches or not.
So value of jwt secret does not matter and simply using the new token works.

<h1>jwt-2</h1>
Similar to jwt-1 but now the secret check is implemented. But in the source provided the jwt-secret is revealed. 
Use that to create verified cookie setting admin to True.

<h1>Kirbytime</h1>
Time based attack vulnerability.



