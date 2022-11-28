import smtplib

email_sender = "youremail@gmail.com"
email_receiver = "receiver@gmail.com"
email_password = "password or app code"
subject = "Hello"
body = "Hi this is a test email using python"

msg = f"Subject: {subject}\n{body}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(email_sender,email_password)

server.sendmail(email_sender,email_receiver,msg)

print("Your email has been sent succesfully")