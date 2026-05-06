import boto3
import logging
from request_process.services.secret import SecretManagerInfo

logger = logging.getLogger("SimpleLogger")
logger.setLevel('INFO')


class DeleteFile:

    def __init__(self):
        self.client = boto3.client('s3')
        self.secrets = SecretManagerInfo()

    def delete_file(self, file_key):
        
        bucket = self.secrets.get_secret()
        
        self.client.delete_object(Bucket=bucket, Key=file_key)
        
        logger.info("deleted from s3")