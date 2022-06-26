class Name:

    def __init__(self, first_name:str, last_name: str) -> None:
        self.first_name = "{0}{1}".format(first_name[0].upper(), first_name[1:].lower())
        self.last_name = "{0}{1}".format(last_name[0].upper(), last_name[1:].lower())

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @property
    def initials(self):
        return "{0}.{1}".format(self.first_name[0], self.last_name[0])


a1 = Name('john', 'SMITH')
print(a1.first_name)
print(a1.last_name)
print(a1.full_name)
print(a1.initials)



