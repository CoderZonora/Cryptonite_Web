Q1 what are the purpose of  __xyz__ double underscored variables stuff in python?

Dunders represent functions called by interpreter in pre-defined - for each dunder - scenario. 
They are used to make use defined types, i.e. user created classes, interact with the rest of python similar to how built-in types behave.
One of the biggest advantages of using Python's magic methods is that they provide a simple way to make objects behave like built-in types. 
That means you can avoid ugly, counter-intuitive, and nonstandard ways of performing basic operators.

Consider a following example:

```
dict1 = {1 : "ABC"}
dict2 = {2 : "EFG"}

dict1 + dict2
Traceback (most recent call last):
  File "python", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
```

This gives an error, because the dictionary type doesn't support addition. Now, let's extend dictionary class and add "__add__" magic method:

```
class AddableDict(dict):

    def __add__(self, otherObj):
        self.update(otherObj)
        return AddableDict(self)


dict1 = AddableDict({1 : "ABC"})
dict2 = AddableDict({2 : "EFG"})

print (dict1 + dict2)
```

Now, it gives following output.

```
{1: 'ABC', 2: 'EFG'}
```

Thus, by adding this method, suddenly magic has happened and the error you were getting earlier, has gone away.
Thus we can use them to override default behaviou to suit our needs instead of having to write our own methods to do the same.


<h2>Important Magic methods:</h2>

__init__: This is a special method in Python classes, it is the constructor method for a class. It’s called when an object is instantiated.

```
class MyClass:
    def __init__(self):
        self.value = 10

obj = MyClass()
print(obj.value)  # Output: 10
```

Used when we have to create new instances of other dunders or classes.

__name__: This is a built-in variable in Python. When the source file is executed as the main program, its __name__ is set to __main__.

Used in pyhthon modules to allow them to be used directly as scripts when required.


__globals__: This is a function that returns a reference to the current global symbol table, which is a dictionary containing all global variables.

Find out about functions which are not normally known 
Eg:

```
def secret_function():
    return "This is a secret function"

def public_function():
    return "This is a public function"

print(public_function.__globals__)
```

__import__: This is a built-in function that invokes the import statement.

Can be used to import required modules.
os_module = __import__('os')

__builtins__: This is a built-in module in Python that contains a collection of common and built-in functions, exceptions, and other objects. You can use it to access functions like print(), import(), etc.

```
print(__builtins__.len([1, 2, 3]))  # Output: 3
```

__call__: It allows a class’s instance to be called as a function, not a method.This can be useful to bypassing restrictions: 
If function calls are restricted in a Python jail, you might be able to use the __call__ method to invoke functions indirectly.


__getattr__: This is a special method that’s called when trying to access a non-existent attribute of an object.

Can be used to bypass filters by joining strings and parameters like:
getattr(x, 'foobar') is equivalent to x.foobar.
The object argument can however also be a string, which allows us to do getattr('__imp'+'ort__', 'open')


__setitem__: This is a special method used for setting a value in a container (like list or dictionary).

```
class Challenge:
    def __init__(self):
        self.whitelist = ['allowed_function']

    def add_to_whitelist(self, item):
        self.whitelist.append(item)

challenge = Challenge()
challenge.whitelist.__setitem__(0, 'secret_function')

```

Can be used to change whitelists and add characters to it.

__delitem__: Bypass blacklists by deleting some items.

```
class SecretContainer:
    def __init__(self):
        self.data = {}

    def __delitem__(self, key):
        del self.data[key]
```

__str__: This is a special method in Python that returns a string representation of an object. 


```
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass object with value {self.value}"

obj = MyClass(10)
print(obj)  # Output: MyClass object with value 10
```
