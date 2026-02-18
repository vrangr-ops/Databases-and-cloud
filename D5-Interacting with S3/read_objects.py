import boto3
import json
import pprint as pp

s3_client =boto3.client("s3")
s3_resource = boto3.resource("s3")
bucket_name = "data-eng-resources"

# #Read object from s3
# s3_object =s3_client.get_object(
#     Bucket=bucket_name,
#     Key="python/chatbot-intent.json"
# )
#
# pp.pprint(s3_object,sort_dicts=False)

#grab a JSON file from a bucket and turn it into a Python dictionary
file_key = "data2.json"  # The path to the file inside the bucket

try:
    # Get the object from S3
    response = s3_client.get_object(Bucket=bucket_name, Key="se-data-folder/burhan/dumps_data2.json")

    # Read the content (the body) of the file
    file_content = response['Body'].read().decode('utf-8')

    # Parse the string into a dictionary
    data2 = json.loads(file_content)

    print(f"Successfully read {data2[3]}'s record!")

except Exception as e:
    print(f"Error: {e}")