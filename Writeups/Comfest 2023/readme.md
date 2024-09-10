Writueps for Comfest ctf

1)Lets Help John

 Just a bunch of headers like User Agent, From etc. Didn't learn anything new.

2) Chicken Daddy : Direct sqli injection. Just had to search about reading arbitrary files in mysql using LOAD_FILE() method and use in UNION query.

3)SIAK-OG : Actually implementation of proto pollution attack in a CTF. Learnt that if there are a lot of key value pairs it might be easier to just set them all to required 
values at the start only like this:

```
payload = json.dumps({
  "__proto__": {
    "admin": True,
    "taken": True,
    "available": True,
    "dummy": {
      "available": True,
      "taken": True
    }
  },
  "DSA": {
    "taken": True
  }
})
```
instead of doing it only for the thing required like this:
```
json={
    "Calculus 1": {"taken": True},
    "DSA": {"taken": True, "available": True, "__proto__": {"available": True, "taken": True}},
    "__proto__": {
        "admin": True,
    },
}
```
Though both are correct.

Copasbin :  checkNpmDeps.js should be run when source given whenever feasible. Helps to narrow down and find implementation of specific vulns.
Also a reminder that innerHTML does not allow inserting <script> tags specifically for XSS. Basically just use <img for XSS even normally.
https://discord.com/channels/1100842688250654732/1100842689148244143/1282364982733836308