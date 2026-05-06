import time
import boto3
import logging
from request_process.services.secret import SecretManagerInfo
# from .file import FileUtils


logger = logging.getLogger("SimpleLogger")
logger.setLevel('INFO')


class UploadFile:

    def __init__(self):
        
        self.client = boto3.client('s3')
        self.secrets = SecretManagerInfo()
        # self.files = FileUtils()

    def upload(self, filename, file_key):
        
        bucket = self.secrets.get_secret()
        logger.info(f'bucket name recieved')
        # print("hell")
        
        # filename = self.files.get_file_path() 
        # logger.info(f'filepath recieved')

        # file_key= self.files.get_file_key(event)

        # logger.info(f'uploading {filename} to s3')
        
        self.client.upload_file(filename, bucket, file_key)
        print("hell")

        logger.info(f'upload complete: {file_key}')
        
        # time.sleep(2)