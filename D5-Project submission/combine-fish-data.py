import boto3
import pandas as pd
import io

s3_client = boto3.client('s3')
bucket_name = 'data-eng-resources'
prefix = 'python/'  # The s3 "folder" where files located

# List of files to process
file_keys = [
    'python/fish-market-mon.csv',
    'python/fish-market-tues.csv',
    'python/fish-market.csv'
]

all_dataframes = []

for key in file_keys:
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        df1 = pd.read_csv(io.BytesIO(response['Body'].read()))

        # Added a column so the origin of the data can be discerned in terms of the original csv file it was pulled from
        df1['Source_File'] = key.split('/')[-1]

        all_dataframes.append(df1)
        print(f"Successfully loaded: {key}")

    except Exception as e:
        print(f"Failed to load {key}: {e}")

# Combine all daily files into one big table
if all_dataframes:
    df2 = pd.concat(all_dataframes)
    print("\nCombined Data Preview:")
    print(df2.head())


# Species and calculate the mean (average)
#Select the variables to average
avg_fish_data = df2.groupby('Species')[['Weight', 'Length1', 'Height', 'Width']].mean()

# 2. Round to 2 decimal places all the variables
avg_fish_data = avg_fish_data.round(2)

# 3. Display the result
print("Average Metrics per Species:")
print(avg_fish_data)


# Prepare buffer data so it is written to csv file
csv_buffer = io.StringIO()
avg_fish_data.to_csv(csv_buffer, index=True) # index=True keeps the 'Species' names

# S3 blucket details
s3_resource = boto3.resource('s3')
target_bucket = 'data-eng-resources'
target_key = 'se-data-folder/fish/burhan/fishy-data.csv'

# 3. Upload the string buffer to S3
try:
    s3_resource.Object(target_bucket, target_key).put(Body=csv_buffer.getvalue())
    print(f"Successfully uploaded data to: {target_bucket}/{target_key}")
except Exception as e:
    print(f"Failed to upload: {e}")

