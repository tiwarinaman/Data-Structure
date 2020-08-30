class stack:
    def __init__(self):
        self.item = []

    def push(self,item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def isEmpty(self):
        return self.item == []

    def get_stack(self):
        return self.item

    def peek(self):
        if not self.isEmpty():
            return self.item[-1]
    def count(self):
        return len(self.item)



