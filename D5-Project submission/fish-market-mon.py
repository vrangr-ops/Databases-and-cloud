import boto3
import pandas as pd
import io

# 1. Setup S3 client
s3_client = boto3.client('s3')
bucket_name = 'data-eng-resources'
file_key = 'fish-market-mon.csv'

# Get the object from S3
response = s3_client.get_object(Bucket=bucket_name, Key="python/fish-market-mon.csv")

# Read the 'Body' into a Pandas DataFrame
# We use BytesIO because S3 returns raw bytes
df = pd.read_csv(io.BytesIO(response['Body'].read()))

# view the fish data
print(df.head())