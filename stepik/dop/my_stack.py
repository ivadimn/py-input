class MyStack:

    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.insert(0, item)

    def pop(self):
        popped_item = self.array.pop(0)
        return popped_item

    def peek(self):
        return self.array[0]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.array):
            raise StopIteration()
        result = self.array[self.index]
        self.index += 1
        return result



stack = MyStack()
stack.push(1)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
for item in stack:
    print(item)
