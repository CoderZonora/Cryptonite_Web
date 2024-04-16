<h1>Juice Shop Challenges Reports:</h1>

DOM XSS: XSS payload in search box.

Error handling: The data erasure feature when opened gives error 

Coupon Bot: Asking 2-3 times gives code

Access confidential document: Checking the robots.txt showed /ftp as disallowed.So went to /ftp to access the files there.

Exposed metrics: Reading the [Prometheus docs](https://prometheus.io/docs/prometheus/latest/getting_started/) tried few of the endpoints and /metrics works. 

Missing encoding: Tried to see why the one photo was not loading, what was differrent about it than others. Firstly, the href had an emoji.
When searching about emojis in links found that they are allowed but need to be [encoded](https://www.w3schools.com/html/html_emojis.asp).
So used and online encoder to url encode the entire src field.
 
Mass dispel: Just reading the [introduction page]() on Juicebox webiste tells you that shift click will close all the notifications at once.

Zero stars: After trying to manipulate using inspect element, finally searched a bit and found had to use BurpSuite. But Burpsuite directly did not accept requests from localhost 
even after setting Proxy in browser settings to the Burpsuite listener (127.0.0.1:8080). Had to toggle the Firefox flag ```network.proxy.allow_hijacking_localhost``` under about:config
to get localhost requests in BurpSuite. There just manipulated the request to set rating to 0.

Forged feedback: Similar to above, 	there is a UserId field in the request, change that to some other user number and challenge solved.

Login admin: Used the tutorial for this. Learnt basic sql injection like -- puts everything after it as comment.Also got the admin email: admin@juice-sh.op

Password Strength: Just guessed the password as hint told it was very simple and the 6th guess was right.Password: admin123

Basket: Just changed GET request from basket/1 to basket/2 

Admin panel: Just searched the word 'admin' in main.js and tried the path. Did not work initially as I was not loged in as admin, but then understood and completed this.
The path was http://127.0.0.1:3000/#/administration

Five-Star Feedback: Once logged into the admin panel, just deleted the five star review.

Login MC safesearch: Got the username from the admin panel.Got his song on searching for his name. The song hinted at two passwords the earlier based on his pet name and the new one. 
First tried the new one but was wrong.Read the challenge and it said that it wanted original password. So tried different combinationa of mr.noodles replacing the 'o' with zeroes.
Then tried one with space (mr. n00dles) and Mr. N00dles worked. 
His new password which he probably did not change later: N3wPassword

Reflected XSS: Initially tried this with the search box like earlier, got an alert but the challenge was not solved.After looking at other pages had to take hint and
 read about the [different types of XSS](https://owasp.org/www-community/attacks/xss/). Could not initially figure out where to add another payload if not the search bar.
 Tried other input fields like new address but did not work. Finally after some time when I was just trying just randomly to see what ordering items does got another 
 vulnerability in the track order page and it was solved.	
 
 Visual Geo Stalking: Got Emma's photo from photo wall as username was E=ma^(2).First searched the photo to know about its owner. From what I found it was owned by Haarleem Government.
 Tried to find som office space near the place in Google Maps but was unsuccessful. Finally while going over the image saw a logo on one of the windows. 
 Searched for the name and it was a company based in Haarleem called ITsec. Tried ITSEC and then ITsec and it worked. New password: Pass1@all
 
 Privacy Policy inspection: I had already noticed some words having a glow in the privacy policy when initially going through it.This challenge showed why.
 After searching for all such words the string it gave was "http://127.0.0.1 We may also instruct you to refuse all reasonably necessary responsibility."
 I initially tried to just concat them all as a string and see if maybe that was an endpoint but that did not work. Had to see the solution.
 So went to http://127.0.0.1:3000/#/We/may/also/instruct/you/to/refuse/all/reasonably/necessary/responsibility and got an error about some jpg not being available.
 Again went to that link and reloded the page. Challenge was solved.
 
 Note for some future challenge: Got an endpoint at http://127.0.0.1:3000/#/juicy-nft to access wallet using ethereum private key.
 
 Register a User as Admin: Intercepted success packet when loggin in as Admin and decoded the JSON token. It had a role parameter as ```"role": "admin"```.
 So when registering new user intercepted the outgoing request and added this in the request body.
 
 CSRF: Does not work with current browsers due to security policies. But understood the approach.
 
 Deluxe Membership: Created a new user. Used negative quantity order to get money in his wallet so that 
 payment button gets enaables in deluxe membership page. Intercepted the request and changed the payment-type from "wallet" to random "card" which worked.
 Later also got to know that any random string would also work.
 
 Forger review: Add a new review, intercept the request and change the username.
 
 Broken Basket: Tried a lot of intercepts changing the JSON packet but none of them seem to work.Tried directly changing just the 
 
 Manipulate basket: Intercepted the request.Directly changing basket id did not work.Had to add another basket id parameter in the same JSON body.
 
 
 Reset Jim's password: Had to see the solution for this. The answer was Samuel and James was supposed to be Captain Kirk from star Trek
 
 Captcha Bypass: I spent quite a while trying to figure out wheather the captcha mechanism had some logical sequence like only havinng captcha answers as Integers less than 10 or something like that.
 That did not work. Seeing the requests found that it was getting the captcha from /rest/captcha endpoint which provided a new captcha id and answer on every request.
 Tried for some time to try to somehow break this but could not.
 Then finally used the Repeater in Burp to just a packet with same Captcha Id and correct answer multiple times and it worked.
 
 
 
 Concepts learned: 
 How to check for sql injections
 Basic sql injection 
 Request forgery
 CSRF vilnerabilities
 XXE
 Problems in:
 Crafting specific sql queries 
 Web3 challenges
 XSS
 
 <h2>Level 3 further:</h2>
 
 
 Database schema: Had to see solutions to understand how to do this.Understood about how to craft SQL queries and how sqlite database schemas work.
 banana')) UNION SELECT sql,2,3,4,5,6,7,8,9 FROM sqlite_master--
 
 XSS: Sent POST to /api/Users with body as :email": "<iframe src=\"javascript:alert(`xss`)\">", "password": "xss"}`. On opening the user list from admin panel challenge was solved.
 Api-Only XSS - Sent POST request to /api/Products {"name": "XSS", "description": "<iframe src=\"javascript:alert(`xss`)\">", "price": 47.11}
 
 Product Description: Sent PUT request to http://127.0.0.1:3000/api/Products/9 with body as 
 {"description":"O-Saft is an easy to use tool to show information about SSL certificate and tests the SSL connection according given list of ciphers and various SSL configurations. <a href=\"https://owasp.slack.com\" target=\"_blank\">More...</a>"}
 
 Upload Size: Upload a 150kB file in the Profile page, then resend the request by changing the endpoint to file-upload.
 
 Chris: Once I got the Users table, just searched for chris , got his email chris.pike@juice-sh.op and used the injeciton in the login page to login.
 
 <h2>Level 4:</h2>
 
 Users Credentials: banana')) UNION SELECT id, email, password, '4', '5', '6', '7', '8', '9' FROM Users--
 
 Christmas: The Products Table has a DeletedAt field that means that products are never actually removed from database just simply not returned normmally. 
 Used the search paramater at http://127.0.0.1:3000/rest/products/search?q= with http://127.0.0.1:3000/rest/products/search?q='))--
 as the query to retrieve the entire product list.If the '))-- is not included the product list is returned but it iis simply the local cached list and not from the actual database 
 From the list got the ProductID of the Christmas Surprise, edited the query to add items to basket and thus successfully added the item to basket.
 
 Expired Coupon: Had to look up how to get an expired coupon.Searched for campaign in the main.js file to get coupon codes.
 Read the function handling the coupon check and it was just a comparision with current date and date mentioned. So used the oldest trick in the book, changed my computer's time to match coupon's time(After running it thrrough https://timestamp.online/ to convert) and it worked.
 
