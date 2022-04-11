from emul import Message
from typing import Callable


class Command:

    def __init__(self, command: str, sender: Callable):
        self.__command = command
        self.__sender: Callable = sender

    def handle_text(self, id: int, text: str):
        self.__sender(id, text)


class Session:
    __msg = Message()

    def __init__(self, id: int, name: str):
        self.__id = id
        self.__name = name
        self.__command: Command = None

    def handle_command(self, command: str):
        self.__command = Command(command, Session.__msg.print_message)

    def handle_text(self, text: str):
        self.__command.handle_text(self.__id, text)

    def __repr__(self):
        return "ID: {0}, name: {1}".format(self.__id, self.__name)


if __name__ == "__main__":
    ses = Session(5252262, "Bob")
    ses.handle_command("/lowprice")
    ses.handle_text("Какой то город")