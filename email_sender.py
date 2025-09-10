import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

def send_email(recipient, filepath):
    sender_email = "swaruchavan6@gmail.com"       # 🔹 your Gmail
    password = ""              # 🔹 Gmail App Password (not normal password!)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = "Automated Web Scraping Report"

    body = "Hello,\n\nPlease find the attached web scraping report.\n\nRegards,\nAutomation Bot"
    msg.attach(MIMEText(body, 'plain'))

    # Attach report
    filename = os.path.basename(filepath)
    with open(filepath, "rb") as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={filename}")
        msg.attach(part)

    # Gmail SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print(f"✅ Email sent to {recipient}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
