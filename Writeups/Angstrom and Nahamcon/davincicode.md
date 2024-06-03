<h1> Davincicode - Nahamcon Web</h1>

Fetching via GET getds the normal webpage but we also see in the source that there is another method in the '/' route called PROPFIND.

So what is PROPFIND?
PROPFIND — used to retrieve properties, stored as XML, from a web resource.
It is also overloaded to allow one to retrieve the collection structure (a.k.a. directory hierarchy) of a remote system.
GET actually retrieves the resource. HEAD is similar to GET except that the message body is not returned. That is, it gets the file header information and not the entire resource.
It appears that PROPFIND differs from HEAD in that properties data stored as XML is returned in the message body (of the packet) rather than attempting to return the entire resource

So accessing via the PROPFIND method gives us the directory /the_secret_dav_inci_code
going to /the_secret_dav_inci_code with propfind again we get /the_secret_dav_inci_code/flag.txt
Now cannot use PROPFIND again as it does not give the actual data of a file.
So have to move the file from the above directory to static and then a GET request to /static/the_secret_dav_inci_code/flag.txt to get the flag.