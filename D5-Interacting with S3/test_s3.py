import boto3

import pprint as pp

s3_client =boto3.client("s3")
s3_resource = boto3.resource("s3")

#list bucket
bucket_list = s3_client.list_buckets()

#pp.pprint(bucket_list)

for bucket in bucket_list ["Buckets"]:
    print(bucket["Name"])

#output bucket contents
bucket_name = "data-eng-resources"
bucket_contents = s3_client.list_objects_v2(
    Bucket=bucket_name
)
pp.pprint(bucket_contents)
