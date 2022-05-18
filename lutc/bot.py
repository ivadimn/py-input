from session import Session
import pickle
import shelve

sessions = { 12345: Session(12345, "Bob"),
    23456: Session(23456, "Pete"),
    34567: Session(34567, "Ann"),
    45678: Session(45678, "Jack")}




def load_sessions() -> dict:
    with open("sessions.pkl", "rb") as f:
        s = pickle.load(f)
    return s


def save_session(key: str, session: Session) -> None:
    db = shelve.open("session1.db")
    db[key] = Session
    db.close()

class Bot:

    def __init__(self):
        self.__sessions = list()

    def handle_command(self, id: int, command):
        session = sessions.get(id)
        if session:
            session.handle_command(command)



"""
db = shelve.open("session1.db")
for k, v in sessions.items():
    db[str(k)] = v
db.close()
"""

db = shelve.open("session.db")
for k, v in db.items():
    print(k, v, type(v))
db.close()


