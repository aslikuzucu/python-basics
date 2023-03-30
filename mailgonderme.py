import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback

mesaj = MIMEMultipart()

mesaj["From"] = "senin mail adresin"
mesaj["To"] = "gonderecegin kisiin maili"
mesaj["Subject"] = "Smtp ile mail gondermek"

yazi = """Python smtp modulu ile mail gonderiyorum.


"""
mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.outlook.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("senin mail adresin","sifren")
    mail.sendmail(mesaj["From"],mesaj["To"], mesaj.as_string())
    print("Mail basarıyla gonderildi")
    mail.close()

except Exception as e:
    print("Bir hata olustu: ", e)
    traceback.print_exc()
