from _queue import Empty


class Queue:
    DEFAULT_CAPACITY = 2

    def __init__(self):
        self.__queue = [None]*Queue.DEFAULT_CAPACITY
        self.__size = 0
        self.__front = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return len(self.__queue) == 0

    def add(self, element):
        if self.__size == len(self.__queue):
            self.__resize(2*len(self.__queue))
        position = (self.__front + self.__size) % len(self.__queue)
        self.__queue[position] = element
        self.__size = self.__size+1

    def pop(self):
        # Critical operation
        if self.is_empty():
            raise Empty('Queue is empty')
        else:
            first_element=self.__queue[self.__front]
            self.__queue[self.__front] = None
            self.__front=(self.__front+1) % len(self.__queue)
            self.__size=self.__size-1
            print ('Position of the first element', self.__front) # Delete in case of serious job
            return first_element

    def first(self):
        if self.is_empty():
            raise(Empty('Queue is empty'))
        else:
            return self.__queue[self.__front]

    def __resize(self, new_capacity):
        print('The queue has been resized')# Delete in case of serious work
        old=self.__queue
        self.__queue = [None]*new_capacity
        position = self.__front
        for i in range(self.__size):
            self.__queue[i] = old[position]
            position = (1 + position) % len(old)
        self.__front = 0


if __name__ == '__main__':
    myQueue = Queue()

    if myQueue.is_empty():
        print('Queue is empty')

    myQueue.add(1)
    myQueue.add(2)
    myQueue.add(3)

    print('myQueue.pop()', myQueue.pop())

    print('What is the first element now?')
    print('myQueue.first()', myQueue.first())

    print('What is the length now?')
    print(len(myQueue))

    myQueue.add(5)
    myQueue.add(6)
    myQueue.add(7)

    print('What is the length now?')
    print(len(myQueue))
