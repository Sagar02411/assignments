import boto3
import pandas as pd
import logging
from io import StringIO
from request_process.services.secret import SecretManagerInfo

logger = logging.getLogger("SimpleLogger")
logger.setLevel('INFO')

class Read:
    
    def __init__(self):        
        self.client = boto3.client('s3')
        self.secrets = SecretManagerInfo()

    def read_file(self, file_key):    
        bucket = self.secrets.get_secret()
        obj = self.client.get_object(Bucket=bucket, Key=file_key)
        body = obj["Body"].read().decode("utf-8")
        dataframe = pd.read_csv(StringIO(body))
        return dataframe

#     s3 = boto3.resource('s3')
# bucket = s3.Bucket('test-bucket')
# # Iterates through all the objects, doing the pagination for you. Each obj
# # is an ObjectSummary, so it doesn't contain the body. You'll need to call
# # get to get the whole body.
# for obj in bucket.objects.all():
#     key = obj.key
#     body = obj.get()['Body'].read()