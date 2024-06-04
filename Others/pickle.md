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

- C++ - There is no standard way to do it.

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