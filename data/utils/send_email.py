import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask
# Email details
sender_email = "sudaisazlan161@gmail.com"
receiver_email = "sudaisazlan09@gmail.com"
password = "obytambizqfamict"

# Create the email
subject = "Test Email from Python"
body = "Hello! This is a test email sent using Python's internal libraries. I am Sudais Axlan"

# Create a MIME object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the email body
message.attach(MIMEText(body, "plain"))

try:
    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Use the appropriate SMTP server and port
        server.starttls()  # Start TLS encryption
        server.login(sender_email, password)  # Log in to your email account
        server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
