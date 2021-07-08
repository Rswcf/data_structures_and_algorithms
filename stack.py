
class Stack(object):
    '''Stack'''
    def __init__(self):
        self.__list = []

    def push(self, item):
        '''Add a new item to the top of the stack'''
        self.__list.append(item)

    def pop(self):
        '''Remove the item at the top of the stack'''
        return self.__list.pop()

    def peek(self):
        '''Return the item at the top of the stack'''
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        '''Determine if the stack is empty'''
        return self.__list == []

    def size(self):
        '''Return the number of the items '''
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
