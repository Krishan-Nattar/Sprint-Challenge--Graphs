
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

moves_934 = ['w', 'n', 'w', 'w', 's', 'n', 'w', 's', 's', 's', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'n', 's', 'e', 'n', 'e', 'e', 'e', 's', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 's', 's', 's', 's', 's', 's', 's', 'e', 's', 'n', 'e', 's', 's', 's', 'w', 'e', 'n', 'e', 'w', 'n', 'n', 'w', 'w', 's', 'w', 'e', 'n', 'n', 'n', 'n', 'w', 's', 'w', 's', 's', 'w', 'e', 'n', 'w', 'e', 'n', 'e', 's', 's', 'n', 'n', 'n', 'e', 'n', 'n', 'w', 's', 'w', 's', 'w', 's', 'n', 'e', 'n', 'w', 'w', 's', 's', 'w', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'n', 'n', 'n', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 's', 's', 's', 'e', 'w', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 'w', 'e', 'e', 'n', 'w', 'e', 'e', 'e', 'e', 'n', 'w', 'w', 'n', 's', 'w', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'n', 'w', 'w', 'n', 'w', 'e', 's', 'e', 'n', 'n', 'w', 'n', 'w', 'e', 'e', 'n', 'n', 's', 'w', 'w', 'e', 'n', 's', 'e', 'e', 'e', 'e', 'n', 'w', 'w', 'e', 'e', 'e', 's', 'n', 'n', 'w', 'w', 'w', 'n', 'n', 's', 'w', 'w', 'w', 'e', 's', 'n', 'e', 'n', 'n', 's', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'e', 's', 'w', 'e', 'e', 'e', 'e', 'n', 'w', 'n', 'w', 'e', 's', 'w', 'e', 'e', 's', 'e', 'n', 's', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'n', 'w', 'e', 'n', 'n', 's', 'e', 'n', 'n', 'w', 'n', 'n', 'w', 'n', 'e', 'w', 'w', 'e', 's', 'e', 's', 's', 'e', 'n', 'n', 'n', 'e', 'w', 'n', 'e', 'n', 'n', 's', 's', 'w', 'w', 'n', 'n', 's', 'w', 'n', 's', 'e', 's', 'w', 'w', 'w', 's', 'w', 'e', 'n', 'w', 'w', 'n', 's', 'e', 'n', 's', 'e', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 's', 'e', 'e', 'e', 'n', 'n', 'n', 'e', 'n', 'w', 'w', 'e', 'e', 's', 'e', 'n', 'e', 'e', 'w', 'w', 's', 's', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 'e', 'n', 'e', 'n', 'e', 'e', 'w', 's', 'n', 'w', 'n', 's', 's', 'w', 'n', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 'e', 'n', 's', 'e', 'w', 'w', 'n', 's', 'w', 's', 'e', 'w', 'w', 's', 'e', 'w', 'w', 'n', 's', 'w', 'w', 's', 'e', 'e', 'w', 'w', 's', 's', 's', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 'n', 'w', 'w', 'n', 'w', 'e', 'n', 'n', 's', 's', 's', 'w', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 'e', 'e', 'n', 'n', 's', 's', 'e', 'n', 'n', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 's', 's', 's', 'w', 'w', 'e', 'e', 'e', 's', 'e', 'n', 's', 'e', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'e', 'e', 'n', 'n', 'n', 'w', 'n', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 's', 'w', 'n', 's', 'e', 's', 'e', 's', 's', 'e', 's', 'e', 'n', 'e', 'n', 'e', 'n', 'e', 'n', 'n', 'e', 'n', 'n', 'e', 'e', 'n', 's', 'e', 'e', 'w', 'n', 's', 'w', 'w', 'n', 's', 'w', 's', 's', 'w', 'n', 's', 's', 's', 'w', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 's', 'w', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 's', 'e', 'e', 'n', 'e', 'n', 'e', 'n', 'n', 'e', 'e', 'n', 'e', 'w', 's', 'w', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 's', 's', 'w', 's', 'e', 's', 'n', 'e', 'e', 'e', 'w', 'n', 'e', 'w', 's', 'w', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'w', 'w', 's', 'w', 's', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 'w', 'n', 'w', 's', 'n', 'w', 'w', 's', 's', 's', 'n', 'n', 'e', 's', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 's', 'e', 'e', 's', 'n', 'e', 'w', 'w', 'w', 's', 's', 'e', 'e', 'w', 'n', 's', 'w', 's', 'e', 'e', 'w', 'w', 's', 'e', 'e', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 'w', 'w', 's', 'e', 'w', 'n', 'n', 'w', 'n', 'w', 'w', 's', 'e', 'w', 's', 'e', 's', 'n', 'w', 's', 's', 's', 's', 's', 's', 'n', 'e', 's', 's', 'w', 's', 's', 'n', 'n', 'e', 's', 's', 's', 'w', 's', 'n', 'e', 's', 's', 'n', 'n', 'n', 'n', 'e', 'e', 'e', 'n', 'e', 's', 's', 'n', 'n', 'e', 'e', 'w', 's', 's', 's', 's', 'n', 'n', 'e', 'w', 'n', 'n', 'w', 'w', 's', 'w', 'w', 's', 's', 's', 'n', 'n', 'e', 's', 's', 'n', 'n', 'e', 's', 's', 'n', 'n', 'w', 'w', 'n', 'w', 'n', 'n', 'n', 'w', 'n', 'n', 'n', 'e', 's', 's', 'n', 'n', 'e', 's', 's', 'e', 's', 'e', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 's', 's', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 'n', 'w', 'w', 'n', 'w', 'w', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 's', 'n', 'e', 'e', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'n', 's', 'e', 's', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'w', 's', 'n', 'e', 's', 'n', 'n', 'e', 'e', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'n', 'n', 'w', 'n', 's', 's', 'w', 'e', 'n', 'w', 'w', 's', 'w', 's', 's']
