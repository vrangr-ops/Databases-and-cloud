import boto3
import pandas as pd
import io

#  S3 connection settings
s3_client = boto3.client('s3')
bucket_name = 'data-eng-resources'
file_key = 'se-data-folder/fish/burhan/fishy-data.csv'

# access the file from S3
response = s3_client.get_object(Bucket=bucket_name, Key="se-data-folder/fish/burhan/fishy-data.csv")

# Read the 'Body' stream
# We use io.BytesIO because the body is a stream of bytes
file_body = response['Body'].read()
df = pd.read_csv(io.BytesIO(file_body))

#View data
print(df.head())