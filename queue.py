class Queue(object):
    '''Queue'''

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        '''Add an item to the end of the queue'''
        self.__list.append(item)

    def dequeue(self):
        '''Remove the item from the top of the queue '''
        return self.__list.pop(0)

    def is_empty(self):
        '''Determine if the queue is empty'''
        return self.__list == []

    def size(self):
        '''Return the number of items in the queue'''
        return len(self.__list)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
