# from pydantic_settings import BaseSettings
# from dotenv import load_dotenv
# import os
# load_dotenv()

# SECRET_KEY = os.getenv("SECRET_KEY", "")
# GMAIL_USER = os.getenv("GMAIL_USER")
# GMAIL_PASS = os.getenv("GMAIL_PASSWORD")
# BASE_URL   = os.getenv("BASE_URL")


# # class Settings(BaseSettings):
# #     DATABASE_URL: str
# #     JWT_SECRET: str
# #     JWT_ALGORITHM: str
# #     REDIS_URL: str = "redis://localhost:6379/0"
# #     MAIL_USERNAME: str
# #     MAIL_PASSWORD: str
# #     MAIL_FROM: str
# #     MAIL_PORT: int
# #     MAIL_SERVER: str
# #     MAIL_FROM_NAME: str
# #     MAIL_STARTTLS: bool = True
# #     MAIL_SSL_TLS: bool = False
# #     USE_CREDENTIALS: bool = True
# #     VALIDATE_CERTS: bool = True
# #     DOMAIN: str

# # Config = Settings()

# # broker_url = Config.REDIS_URL
# # result_backend = Config.REDIS_URL
# # broker_connection_retry_on_startup = True