class Deque(object):
    '''Doubly Ended Queue'''
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        '''Add an item to the top of the queue'''
        self.__list.insert(0, item)

    def add_rear(self, item):
        '''Add an item to the end of the queue'''
        self.__list.append(item)

    def pop_front(self):
        '''Remove the item from the top of the queue'''
        return self.__list.pop(0)

    def pop_rear(self):
        '''Remove the item from the end of the queue'''
        return self.__list.pop()

    def is_empty(self):
        '''Return the number of items of the queue'''
        return len(self.__list)

if __name__ == '__main__':
    q = Deque()
    q.add_front(1)
    q.add_front(2)
    q.add_rear(3)
    q.add_rear(4)
    print(q.pop_rear())
    print(q.pop_front())
    print(q.pop_rear())
    print(q.pop_front())
