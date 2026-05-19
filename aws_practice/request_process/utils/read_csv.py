import boto3
import pandas as pd
from io import StringIO

s3_client = boto3.client("s3")

def read_csv_from_s3(bucket, key):
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    body = obj["Body"].read().decode("utf-8")
    dataframe = pd.read_csv(StringIO(body))
 
    return dataframe