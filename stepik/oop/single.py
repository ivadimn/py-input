class Single:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = "any data"


c1 = Single()
print(c1.data)
c2 = Single()
print(id(c1))
print(id(c2))
