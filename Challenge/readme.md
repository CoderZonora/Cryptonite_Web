<h1>Challenge Report</h1>

The challenge is hosted at http://20.193.136.145:1337 on my Azure virtual machine.

The site is a small book library holding upto 10 books with their name, author name and nummber of pages.It has a login form and registration and logging in is required by registering a user.
On logging in it gets 5 random books. There are options to Add books and a search feature.

Liteshare: On clicking a book's name in the library a page opens up with the url as : ip:1337/liteShare/<username>/bookId. 
If logged in as another user and open the url a report option with input for reason for report comes up.

The application is not using any database engine but instead is storing the books as Javascript objects under the class newBook.

On going thorugh the javascript file afterr logging in we see somme endpoints defined. The /stats and /report seem interesting. 
/stats upon opening gives a JSON response where we can see the headers set for this application.
The X-XSS-Protection is set to 0 and CSP is set to : ```default-src 'self' openlibrary.org;img-src 'self' raw.githubusercontent.com external-content.duckduckgo.com;base-uri 'self';font-src 'self' https: data:;form-action 'self';frame-ancestors 'self';object-src 'none';style-src 'self' https: 'unsafe-inline'```
These show potential methods of inflitrating the application using CSP bypass ans XSS.

There are many methods of CSP bypass so am looking into which particular method will work for this application.
Going thorugh https://book.hacktricks.xyz/pentesting-web/content-security-policy-csp-bypass.

JSONP seems like a possible exploit to run javascript code.Trying to figure out how it works and what payload I can use.	
Also reading other possible methods to exploit.
