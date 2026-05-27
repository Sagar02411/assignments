import smtplib
from email.mime.text import MIMEText
from app.core.config import settings
 
def send_verification_email(user_email: str,token: str):
    verification_link = (f"https://proglottidean-premorally-jaxson.ngrok-free.dev/verify-email?token={token}")

    body = f"""Welcome! Click below to verify your email: {verification_link}"""
 
    msg = MIMEText(body)
    msg["Subject"] = "Verify Your Email"
    msg["From"] = settings.MAIL_USERNAME
    msg["To"] = user_email

#creating SMTP SERVER
    server = smtplib.SMTP(settings.MAIL_SERVER,settings.MAIL_PORT)
    server.starttls()

    server.login(settings.MAIL_USERNAME,settings.MAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
