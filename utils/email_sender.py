import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to_email: str, subject: str, body: str):
    from_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")
    
    # Set up the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)
    
    # Create the email
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    # Send the email
    server.sendmail(from_email, to_email, message.as_string())
    server.quit()
