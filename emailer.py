import smtplib

content = ""
email = ""
password = ""
receiver = ""

mail = smtplib.SMTP("smtp.gmail.com", 587)

mail.ehlo()

mail.starttls()

mail.login(email, password)

mail.sendmail(email,receiver, content)

mail.close()

