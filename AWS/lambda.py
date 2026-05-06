# import os 
# import boto3
# import botocore
# import json
from urllib.parse import unquote_plus
# from loguru import logger
# import pandas as pd
# import time 
# from botocore.exceptions import ClientError

# client = boto3.client('s3')

# def lambda_handler(event, context):
#     secret_name = "vb-python-intern-secret1"
#     region_name = "ap-northeast-1"
#     session = boto3.session.Session()
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )
#     try:
#         get_secret_value_response = client.get_secret_value(
#         SecretId=secret_name
#     )
#     except ClientError as e:
#         raise e
#     secret = get_secret_value_response['SecretString']
#     secrets = json.loads(secret)
#     print(type(secret))
#     print(secret)
#     print(type(secrets))
#     key, value = list(secrets.items())[0]
#     bucket = value
#     print(bucket)
    
#     try:
#         cur_path = os.getcwd()
#         key, value = list(event.items())[0]
#         file = value
#         filename = os.path.join(cur_path, 'data', file)
#         data = open(filename, 'rb')
#         logger.info(f'Uploading {filename} to s3')
#         client = boto3.client('s3')
#         client.upload_file(filename, bucket, file)
#         logger.info(f'uploaded {filename} to s3')
#         time.sleep(2)
#         df = pd.read_csv(filename)
#         logger.info(df.head(5))            
#         time.sleep(2)
#         try:
#             client.delete_object(Bucket=bucket, Key=value)
#             logger.info(f'uploaded file {event} deleted')
#         except Exception as e:
#             logger.error(f"error : {str(e)}")
#         return {
#             "statusCode": 200,
#             "message": "file uploaded successfully"
#         }

#     except Exception as e:
#         logger.error(f"Failed to upload file to S3: {str(e)}")
#         return {
#             "statusCode": 400,
#             "message": "failed to upload"
#         }

# # event = 'xyz.csv'



# lambda_handler(event, context)

import logging
from request_process.main import Process

logger = logging.getLogger("SimpleLogger")
logger.setLevel('INFO')

def lambda_handler(event, context):
    try:
        p = Process(event)
        p.run()
        return {
            "status code": 200,
            "message": "function completed"
        }    
    except Exception as e:
        logger.error(f"error in lambda handler: {str(e)}")
        
        return {"statusCode": 400,
                "message": str(e)}

context = ''

event = {"file": "xyz.csv"}

lambda_handler(event, context)