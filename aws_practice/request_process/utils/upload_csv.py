import boto3
import os
from request_process.utils.logger import logger
 
s3_client = boto3.client("s3")
def upload_file(bucket):
    cur_path = os.getcwd()
    file = "test.csv"
    file_path = os.path.join(cur_path, "files", file)
 
    logger.info(f"uploading {file_path} to {bucket}")
    s3_client.upload_file(file_path, bucket, file)