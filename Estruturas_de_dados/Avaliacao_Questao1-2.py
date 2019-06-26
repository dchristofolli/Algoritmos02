class Fila:
    def __init__(self, size=100):
        self.data = [None] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.tail < len(self.data):
            self.data[self.tail] = value
            self.tail += 1
        else:
            raise Exception("Fila cheia")

    def dequeue(self, value):
        if self.tail == self.head:
            raise Exception("Fila vazia.")
        self.head = value
        self.head += 1
        return self.head
