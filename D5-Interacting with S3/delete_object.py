import boto3
import json
import pprint as pp

s3_client =boto3.client("s3")
s3_resource = boto3.resource("s3")
bucket_name = "data-eng-resources"

del_response =s3_client.delete_object(
    Bucket=bucket_name,
    Key="se-data-folder/burhan/data.json"
)

pprint(del_response
       )