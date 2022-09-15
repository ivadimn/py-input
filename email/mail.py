import smtplib

vadimn = "WV2mrczR7jLirWjsmp1R"
pickup = "9NQsHFmqmeYCynFEf9QE"

class Mail:

    def __init__(self, sender: str):
        self.__sender = sender
        self.__server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
        self.__message = []
        self.__attachment = []

    def prepare(self, subject: str, mbody: str, attachments: list = None) -> None:
        self.__message.append(subject)
        self.__message.append(mbody)

    def send(self, destination: str) -> bool:
        try:
            self.__server.login(self.__sender, pickup)
            self.__server.sendmail(self.__sender, destination, "\n".join(self.__message))

            return True
        except Exception as ex:
            print(str(ex))
            return False
        finally:
            self.__server.quit()


if __name__ == "__main__":
    #mail = Mail("pickup.music@mail.ru")
    subj, body = input("Вседите сообщение: ").split()
    print(subj, body)
    #mail.prepare(subj, body)
    #print(mail.send("ivadimn@mail.ru"))
