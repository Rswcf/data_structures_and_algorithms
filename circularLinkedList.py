class Node(object):
    '''节点'''

    def __init__(self, elem):
        self.elem = elem
        self.next = None


# node = Node(100)

class circularLinkedList(object):
    '''循环链表'''

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''length of the linked list'''
        if self.is_empty():
            return 0

        # cur游标，用来移动遍历节点
        cur = self.__head
        # count记录
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        '''traversal of the linked list'''
        if self.is_empty():
            return
        cur = self.__head
        while cur.next != self.__head:
            print(cur.elem, end=' ')
            cur = cur.next
        # 退出循环，cur指向尾节点，但尾节点的元素未打印
        print(cur.elem)

    def add(self, item):
        '''add an item to the top of the linked list'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next

            node.next = self.__head
            self.__head = node
            # cur.next = node
            cur.next = self.__head


    def append(self, item):
        '''add an item to the end of the linked list'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # node.next = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        '''insert the itemsto the specified position of the linked list'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:

            pre = self.__head
            count = 0
            while count <= (pos - 1):
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''delete the item in the list'''
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                # 先判断此节点是否是头节点
                # 头节点
                if cur == self.__head:
                    # self.__head = cur.next
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head

                else:
                    # 中间节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                self.__head = None
            else:
                #pre.next = cur.next
                pre.next = self.__head

    def search(self, item):
        '''search the the item in the list'''
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.item == item:
            return True

        return False


if __name__ == '__main__':
    ll = circularLinkedList()
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
    ll.travel()


    ll.remove(1000)

    ll.travel()
