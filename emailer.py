import smtplib

#Comments
content = ""

#Sender's email
email = ""

#Password to sender's email
password = ""

#receiver email
receiver= ""

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()

mail.starttls()

mail.login(email, password)

mail.sendmail(email,receiver, content)

mail.close()

