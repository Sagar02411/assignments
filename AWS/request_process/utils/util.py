from dotenv import load_dotenv
import os

load_dotenv()

region_name = os.getenv('REGION_NAME')
secret_name = os.getenv('SECRET_NAME')