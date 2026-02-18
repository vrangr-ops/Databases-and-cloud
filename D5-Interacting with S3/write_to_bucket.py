import boto3
import pprint as pp
import json

s3_client =boto3.client("s3")
s3_resource = boto3.resource("s3")
bucket_name = "data-eng-resources" #turning the name of the s3 bucket name into a variable

# #write to bucket (uploading/changing data on cloud storage s3) by creating a file
# dict_to_upload = {"name": "Burhan","status": 1}
# with open ("data.json","w") as jsonfile:
#     json.dump(dict_to_upload,jsonfile) #dumps python dictionary into a json file

##upload the json file to s3 bucket
# s3_client.upload_file(
#     Filename="data.json", #local name of file
#     Bucket= bucket_name, #the bucket that the file will be uploaded to
#     Key="se-data-folder/burhan/data.json"
# )

#write to a s3 bucket without making a local file- internal dictionary
dict_to_upload = [
    {
        "first_name": "Burhan",
        "last_name": "Uddin",
        "status": 1
    },
    {
        "first_name": "Bob",
        "last_name": "Smith",
        "status": 0
    },
    {
        "first_name": "Molly",
        "last_name": "Smith",
        "status": 0
    },
    {
        "first_name": "Bob",
        "last_name": "Marley",
        "status": 0
    },
]
s3_client.put_object(
    Body=json.dumps(dict_to_upload),
    Bucket=bucket_name,
    Key="se-data-folder/burhan/dumps_data2.json"

)
