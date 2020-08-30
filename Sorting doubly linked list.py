class node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.start = None

    def insert(self,value):
        new_node = node(value)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next !=None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp.next
    def sort_list(self):
        if self.start is None:
            print('Empty linked list')
        else:
            temp = self.start
            while temp != None:
                p1 = self.start
                p2 = p1.next
                while p2 != None:
                    if p1.data > p2.data:
                        T = p1.data
                        p1.data = p2.data
                        p2.data = T
                    p1 = p2
                    p2 = p2.next
                temp = temp.next



    def view_list(self):
        if self.start is None:
            print('Empty Doubly linked list')
        else:
            temp = self.start
            while temp != None:
                print(temp.data,end=' ')
                temp = temp.next

d = DoublyLinkedList()
d.insert(5)
d.insert(2)
d.insert(10)
d.insert(3)
d.view_list()
print()
d.sort_list()
d.view_list()
