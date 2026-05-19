import os
from dotenv import load_dotenv

load_dotenv()
SECRET_NAME = os.getenv('SECRET_NAME')
AWS_REGION = os.getenv('AWS_REGION')