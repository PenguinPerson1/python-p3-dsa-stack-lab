class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return not len(self.items)

    def push(self, item):
        if self.size() < self.limit:
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]
    
    def size(self):
        return len(self.items)

    def full(self):
        return not self.size() < self.limit

    def search(self, target):
        count=self.size()
        for item in self.items:
            count = count - 1
            if item == target: return count
        return -1
