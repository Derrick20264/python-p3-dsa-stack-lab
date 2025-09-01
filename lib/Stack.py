class Stack:
    def __init__(self, items=None, limit=100):
        # Initialize stack with existing list or empty list
        if items is None:
            self.items = []
        else:
            self.items = list(items)  # make a copy to avoid modifying original
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) >= self.limit:
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            # distance from top (top = 0)
            index_from_top = len(self.items) - 1 - self.items[::-1].index(target)
            return len(self.items) - 1 - index_from_top
        except ValueError:
            return -1
