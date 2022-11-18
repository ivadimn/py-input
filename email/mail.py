import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
import config


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
        self.__message.attach(MIMEText(mbody))
        for file in attachments:
            filename = os.path.basename(file)
            mmtype, enccoding = mimetypes.guess_type(file)
            file_type, subtype = mmtype.split("/")
            if file_type == "text":
                with open(file, "r") as f:
                    file = MIMEText(f.read())
            elif file_type == "image":
                with open(file, "rb") as f:
                    file = MIMEImage(f.read(), subtype)
            elif file_type == "audio":
                with open(file, "rb") as f:
                    file = MIMEAudio(f.read(), subtype)
            elif file_type == "application":
                with open(file, "rb") as f:
                    file = MIMEApplication(f.read(), subtype)
            else:
                with open(file, "rb") as f:
                    file = MIMEBase(file_type, subtype)
                    file.set_payload(f.read())
                    encoders.encode_base64(file)

            file.add_header('content-disposition', 'attachment', filename=filename)
            self.__message.attach(file)

    def send(self, destination: str) -> bool:
        try:
            self.__server.login(self.__sender, config.PICKUP)
            self.__message["To"] = destination
            self.__server.sendmail(self.__sender, destination, self.__message.as_string())
            return True
        except Exception as ex:
            print(str(ex))
            return False
        finally:
            self.__server.quit()


def get_files(dirs: str) -> list:
    file_list = []
    for file in os.listdir(dirs):
        abs_path = os.path.join(os.path.abspath(os.path.curdir), dirs, file)
        mmtype, enccoding = mimetypes.guess_type(file)
        file_type, subtype = mmtype.split("/")
        print(file_type, subtype)
        file_list.append(abs_path)
    return file_list


if __name__ == "__main__":
    mail = Mail("pickup.music@mail.ru")
    subj = input("Введите тему: ")
    body = input("Введите сщщбщение: ")
    mail.prepare(subj, body, [])
    print(mail.send("ivadimn@mail.ru"))

