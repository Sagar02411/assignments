import boto3
s3_client = boto3.client("s3")

def delete_file(bucket, key):
    s3_client.delete_object(Bucket=bucket, Key=key)