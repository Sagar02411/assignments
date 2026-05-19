import boto3
import json
import logging
from botocore.exceptions import ClientError
from request_process.utils.util import region_name, secret_name

logger = logging.getLogger("SimpleLogger")
logger.setLevel('INFO')


class SecretManagerInfo:

    def __init__(self):
        session = boto3.session.Session()
        
        self.client = session.client(service_name='secretsmanager', 
                                    region_name=region_name)

    def get_secret(self):
        
        try:
            response = self.client.get_secret_value(SecretId=secret_name)
            # print(f"secret name {secret_name}")
            
        except ClientError as e:
            
            logger.error(f"error getting secret: {str(e)}")
            
            raise
        
        
        secret = response['SecretString']

        secrets = json.loads(secret)
        
        return list(secrets.values())[0]