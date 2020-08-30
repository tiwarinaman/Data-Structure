class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None

    def InsertLast(self,value):
        new_node = node(value)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            
    def reverse_list(self):
        if self.start is None:
            print('Empty linked list.')
        else:
            p1 = self.start
            p2 = self.start.next
            p3 = p2.next
            p1.next = None
            while p3.next is not None:
                p1 = p2
                p2 = p3
                p3 = p3.next
            p2.next = p1
            p3.next = p2
            self.start = p3
                
        

    def view_list(self):
        if self.start is None:
            print('Empty linked list.')
        else:
            temp = self.start
            while temp is not None:
                print(temp.data,end=' ')
                temp = temp.next


l = LinkedList()
l.InsertLast(10)
l.InsertLast(20)
l.InsertLast(30)
l.view_list()
print()
print('Reverse of the linked list')
l.reverse_list()
l.view_list()
