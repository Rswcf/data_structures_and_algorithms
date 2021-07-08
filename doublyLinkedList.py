class Node(object):
    '''Node'''
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None

class doublyLinkedList():
    '''双链表'''
    def __init__(self, node = None):
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''length of the linked list'''
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录
        count = 0
        while cur != None:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        '''traversal of the linked list'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end= ' ')
            cur = cur.next

        print('')

    def add(self, item):
        '''add an item to the top of the linked list'''
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        '''add an item to the end of the linked list'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        '''insert the itemsto the specified position of the linked list'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next

            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def remove(self,item):
        '''delete the item in the list'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        '''search the the item in the list'''
        cur = self.__head
        while cur.next != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

if __name__ == '__main__':
    ll = doublyLinkedList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6
    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel

    ll.remove(1000)

    ll.travel()