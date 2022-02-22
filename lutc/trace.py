class Wapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print("Trace: {0}".format(attrname))
        return getattr(self.wrapped, attrname)


x = Wapper([1, 2, 3])
x.append[4]

        