import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



vadimn = "WV2mrczR7jLirWjsmp1R"
pickup = "9NQsHFmqmeYCynFEf9QE"

class Mail:

    def __init__(self, sender: str):
        self.__sender = sender
        self.__server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
        self.__message = None
        self.__attachment = []


    def prepare(self, subject: str, mbody: str, attachments: list = None) -> None:
        self.__message = MIMEMultipart()
        self.__message["From"] = self.__sender
        self.__message["Subject"] = subject
        self.__message.attach(MIMEText(body))

    def send(self, destination: str) -> bool:
        try:
            self.__server.login(self.__sender, pickup)
            self.__message["To"] = destination
            self.__server.sendmail(self.__sender, destination, self.__message.as_string())

            return True
        except Exception as ex:
            print(str(ex))
            return False
        finally:
            self.__server.quit()


if __name__ == "__main__":
    mail = Mail("pickup.music@mail.ru")
    subj = input("Введите тему: ")
    body = input("Введите сщщбщение: ")
    print(subj, body)
    mail.prepare(subj, body)
    print(mail.send("ivadimn@mail.ru"))
