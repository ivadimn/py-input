from session import Session

sessions = [
    {12345: Session(12345, "Bob")},
    {23456: Session(23456, "Pete")},
    {34567: Session(34567, "Ann")},
    {45678: Session(45678, "Jack")}
]

class Bot:

    def __init__(self):
        self.__sessions = list()

    def handle_command(self, id: int, command):
        session_list = list(filter(lambda item: id in item.keys(), sessions))
        if len(session_list) > 0:
            session = session_list[0].get(id)
            session.handle_command(command)


s = filter(lambda item: 45678 in item.keys(), sessions)
print(list(s))


