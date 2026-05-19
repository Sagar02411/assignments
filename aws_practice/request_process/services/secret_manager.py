import json
import boto3
import os
from request_process.utils.util import SECRET_NAME, AWS_REGION

secret_cache = None

def get_secret():
    global secret_cache
    if secret_cache:
        return secret_cache
 
    secret_name = SECRET_NAME #os.environ.get("SECRET_NAME")
    region_name = AWS_REGION #os.environ.get("AWS_REGION")

    client = boto3.client("secretsmanager", region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])
    secret_cache = secret
    return secret