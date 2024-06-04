Things I learnt from writeups of GPNCTF:

1)If there is a function which is doing something and you want to prevent it and 
have XSS you can use dunders to change the function's implementation like so:

```
<script>''.__proto__.replace = (a, b) => a</script>
```

This is a piece of JavaScript code that modifies the replace method on the prototype of all strings. Here’s a breakdown of what it does:

''.__proto__: In JavaScript, all objects have a prototype, which is another object that they inherit properties and methods from. The __proto__ property is a reference to this prototype object. In this case, ''.__proto__ refers to the prototype of the String object, because '' is an empty string.
.replace = (a, b) => a: This line is assigning a new function to the replace method on the String prototype. The replace method is used to replace some or all matches of a pattern in a string. The pattern can be a string or a RegExp, and the replacement can be a string or a function to be called for each match. However, this code is replacing the replace method with a new function that simply returns the first argument a, effectively disabling the normal functionality of the replace method for all strings.
So, after this script is run, if you try to call the replace method on a string, it will just return the first argument you pass to it, regardless of what the second argument is.

2) httpOnly prevents javascript to access certain resources such as the cookie. 
That is why it is used when hosting applications.

3) Learn DOM clobbering