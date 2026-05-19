import os
import time

from request_process.utils.logger import logger
from request_process.utils.delete import delete_file
from request_process.utils.upload_csv import upload_file
from request_process.utils.read_csv import read_csv_from_s3
from request_process.services.secret_manager import get_secret

 
def process_request(event):
    try:
        secret = get_secret()
        bucket = secret["S3_bucket"]
        upload_file(bucket)

 
        s3_file_name = event["s3_File_Name"]
        dataframe = read_csv_from_s3(bucket, s3_file_name)
        logger.info(dataframe.head(3))
        time.sleep(2)
        try:
            delete_file(bucket, s3_file_name)
            logger.info(f"Deleted file {s3_file_name}")
        except Exception as delete_err:
            logger.error(f"Error deleting file: {delete_err}")
 
        return {
            "statusCode": 200,
            "body": "Hello from Lambda!"
        }
 
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        return {
            "statusCode": 500,
            "body": "Internal server error"
        }
    