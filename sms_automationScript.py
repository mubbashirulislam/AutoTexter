import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import configparser

def read_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config['EmailConfiguration']

def send_email(subject, body, to_email, attachment_path, sender_email, sender_password, smtp_server, smtp_port):
    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the CV as an attachment
    cv_attachment = MIMEApplication(open(attachment_path, 'rb').read())
    cv_attachment.add_header('Content-Disposition', 'attachment', filename='Mubbashirul Islam-IT Support-CV.pdf')
    message.attach(cv_attachment)

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

if __name__ == "__main__":
    # Read email configuration from the config file
    email_config = read_config()

    # Specify the details for the email
    subject = "Application for entry-level 'IT Support Engineer' position."
    body = """
Dear Hiring Manager,

I am writing to express my interest in the "IT Support Engineer" position at your organization. My comprehensive knowledge and hands-on experience in IT support and networking make me a strong candidate for this role.

I want to emphasize that I am a completely self-learner, acquiring my skills and expertise from the most reputable sources online. My deep understanding of cybersecurity and modern online threats, coupled with my ability to optimize PC performance and implement robust security measures, positions me as a reliable candidate for your team. My passion for technology and continuous self-improvement aligns perfectly with the dynamic nature of the IT industry. I am well-versed in the latest trends in modern technologies and devices, demonstrating my commitment to staying informed and relevant.

I welcome any opportunity for further discussion regarding my candidacy for this position. Please feel free to reach out to me at your convenience, as I am eager to contribute my skills and expertise to the success of your team.

Sincerely, 
Mubbashirul Islam.

"""

    # Specify the path to your CV
    cv_path = "D:\GitHub\Projects\Python\PYTHON\Mubbashirul Islam-IT Support-CV.pdf"

    # Specify the list of recipient email addresses
    recipient_emails = ["callmemubasshir@gmail.com"]

    # Loop through the list of recipients and send the email
    for recipient_email in recipient_emails:
        send_email(subject, body, recipient_email, cv_path,
                   email_config['sender_email'], email_config['sender_password'],
                   email_config['smtp_server'], int(email_config['smtp_port']))

    print("Emails sent successfully.")

