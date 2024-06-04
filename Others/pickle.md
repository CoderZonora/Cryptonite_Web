Q: encoding vs serialisation?

Encoding can be understood as a form of translation of data into some new form which is more useful to carry out a particular task like transmission.
Decoding then is just translating it back into the original form.

An object can be defined as an encapsulated unit of data and behaviour. 
Serialisation is a method to convert complex structures like objects into a data stream in such a way that the object 
in its entirety can be recovered to the state it was in before the serialisation into either 
the same language or into another language thorugh the use of specific deserialisers.What is important is that the entire initial state is recoverable.

An analogy:
Encoding can be thought of as translating a book into a different language. 
For example, you might have a book in English, and you want to make it accessible to people who read French. 
So, you translate (encode) the book into French.
Anyone who can read French (decode) can now understand the book. The content of the book remains the same,
it’s just presented in a different format (language).
Serialization, on the other hand, can be thought of as packing up a book for shipping. 
Suppose you want to send the book to a friend in another city. You can’t send the book as it is,s
you need to package it (serialize it) into a box, ready for transport. When the book reaches your friend,
they unpack the box (deserialize) to get the book back in its original form.
So, while both processes involve changing the format of the data, encoding is more about changing the representation of the data, while serialization is about making the data transportable while preserving its state. 

Q: research the various method to convert an **object in memory** to a file and then read that file back into an object in

- C++ - There is no standard way to do it. Different libraries implement it differently.
 For simple objects we can use built it function like such:
 
 ```
 // C++ Program to illustrate how we can serialize and
// deserialize an object
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

class Serializable {
private:
    string name;
    int age;

public:
    Serializable(){};
    // Constructor to initialize the data members
    Serializable(const string& name, int age)
        : name(name)
        , age(age)
    {
    }

    // Getter methods for the class
    string getName() const { return name; }
    int getAge() const { return age; }

    //  Function for Serialization
    void serialize(const string& filename)
    {
        ofstream file(filename, ios::binary);
        if (!file.is_open()) {
            cerr
                << "Error: Failed to open file for writing."
                << endl;
            return;
        }
        file.write(reinterpret_cast<const char*>(this),
                   sizeof(*this));
        file.close();
        cout << "Object serialized successfully." << endl;
    }

    //  Function for Deserialization
    static Serializable deserialize(const string& filename)
    {
        Serializable obj("", 0);
        ifstream file(filename, ios::binary);
        if (!file.is_open()) {
            cerr
                << "Error: Failed to open file for reading."
                << endl;
            return obj;
        }
        file.read(reinterpret_cast<char*>(&obj),
                  sizeof(obj));
        file.close();
        cout << "Object deserialized successfully." << endl;
        return obj;
    }
};

int main()
{
    // Create and serialize an object
    Serializable original("Alice", 25);
    original.serialize("data.bin");

    // Deserialize the object
    Serializable restored
        = Serializable::deserialize("data.bin");

    // Test the  deserialized object
    cout << "Deserialized Object:\n";
    cout << "Name: " << restored.getName() << endl;
    cout << "Age: " << restored.getAge() << endl;

    return 0;
}

```
But for complex functions using dedicated libraries like Boost or cereal is preffered.

- python:
1) using JSON,YAML or other similar human readable serialisation languages. JSON offers methods like json.dumps() for serialisation and json.loads() for deserialisation.
 Output is human readable and much easier compatiblity between other languages.
2) using the pickle library which uses binary protocol and is not human readable. Faster than JSON but also introduces some security flaws.
3) create custom serialisation using __getstate__() and __setstate__().

- java - 
1) Java has a default method of serialization implemented thorugh the Serializable interface along with the ObjectOutputStream object.
 Only those classes which are marked as serialisable can be serialised or else they will throw a NotSerializableException.
 
2) Custom serialization using the Externalizable interface which has the writeExternal() and readExternal methods.
 Can be useful when trying to serialize an object that has some unserializable attributes. 

3) Using external dependencies like GSON, YAML beans, Jackson to serialize to languages like JSON, YAML etc. 
Each dependencie has its own set of features and benefits for a particular use case.

4) Using binary serialization like Google Protocol buffer (profbus). 

Q: 500 word short note on python pickle
- how does it do the magic i.e. explain the pickled file content structure, what escape characters, sequences start stop bits etc are used

Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
The idea is that this character stream contains all the information necessary to reconstruct the object in another python script.
 
Pickle works by using simple opcodes like ```MARK, STOP, POP, EMPTY_LIST, EMPTY_DICT, EMPTY_TUPLE``` etc. 
Each opcode is followed by arguments required for the operation. 
For example, the BININT opcode is followed by a 4-byte integer, and the BINSTRING opcode is followed by a length and a string of that length.

The byte stream starts with a PROTO opcode followed by a protocol version number (from 0 to 5). 
The FRAME opcode is used in protocol 4 and later to indicate the size of the following frame.
The STOP opcode marks the end of the pickle stream.

So, the magic of pickle is in its ability to convert complex Python objects into a sequence of simple operations 
that can be easily stored and later used to reconstruct the original object. 
However, it’s important to note that pickle is not secure against erroneous or maliciously constructed data. 
 
- what does this pickle unpickle, explain what every character translates, for e.g. if it was bae64 you were given `eyJhbGciO` you would say
ey:`{`
J: `"` and so on
```py
arr = bytes([
    0x80, 0x04, 0x95, 0x1A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5D,
    0x94, 0x28, 0x4B, 0x01, 0x4B, 0x02, 0x7D, 0x94, 0x8C, 0x03, 0x63, 0x61,
    0x74, 0x94, 0x8C, 0x05, 0x6D, 0x6F, 0x75, 0x73, 0x65, 0x94, 0x73, 0x65,
    0x2E
])

```

![output](output.png)


- `0: \x80 PROTO 4`: This sets the pickle protocol to version 4.
- `2: \x95 FRAME 26`: This starts a new frame of 26 bytes.
- `11: ] EMPTY_LIST`: This pushes an empty list onto the stack.
- `12: \x94 MEMOIZE (as 0)`: This stores the top of the stack in memo under index 0.
- `13: ( MARK`: This pushes a mark onto the stack for later building a container object.
- `14: K BININT1 1`: This pushes the integer 1 onto the stack.
- `16: K BININT1 2`: This pushes the integer 2 onto the stack.
- `18: } EMPTY_DICT`: This pushes an empty dictionary onto the stack.
- `19: \x94 MEMOIZE (as 1)`: This stores the top of the stack in memo under index 1.
- `20: \x8c SHORT_BINUNICODE 'cat'`: This pushes the string 'cat' onto the stack.
- `25: \x94 MEMOIZE (as 2)`: This stores the top of the stack in memo under index 2.
- `26: \x8c SHORT_BINUNICODE 'mouse'`: This pushes the string 'mouse' onto the stack.
- `33: \x94 MEMOIZE (as 3)`: This stores the top of the stack in memo under index 3.
- `34: s SETITEM`: This pops a key-value pair from the stack and sets the key-value pair in the dictionary.
- `35: e APPENDS (MARK at 13)`: This appends stack items to a list until (and including) the closest mark object.
- `36: . STOP`: This indicates the end of the pickle stream.



