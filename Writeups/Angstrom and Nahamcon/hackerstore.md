This has two parts. 
Firstly sql injection to get username and password hashes. There is one user called admin also.
Then cracking the hash by using the wordlist provided.
The hash is not any normal md5 or sha256.It is pbkdf2 like this https://www.openwall.com/lists/john-users/2019/03/25/10.
Eg: sha256$8000$XAuBMIYQQogxRg$tRRlz8hYn63B9LYiCd6PRo6FMiunY9ozmMMI3srxeRE

So this gives us the algorithm, number of iterations, salt annd then the actual hash all separated by $.


Final code to crack:


```
import hashlib
import binascii


def pbkdf2_sha256(password, salt, iterations, dklen=None):
    if not dklen:
        dklen = hashlib.sha256().digest_size
    key = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations, dklen
    )
    return key


iterations = 600000
salt = "MSok34zBufo9d1tc"
target = "b2adfafaeed459f903401ec1656f9da36f4b4c08a50427ec7841570513bf8e57"


def trial(password):
    key = pbkdf2_sha256(password, salt, iterations)
    result = binascii.hexlify(key).decode()

    if result == target:
        print(password)
        exit(0)


lst = open("password_list.txt").readlines()
l = len(lst)

for i, p in enumerate(lst):
    trial(p.strip())
    print(f"{i} / {l}", end="\r")
	
	```

Here password_list.txt is provided in challenge and the target hash is found using the sql injection. Thus logging in as admin gives flag.