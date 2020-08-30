class node:
    def __init__(self,data):
        self.data =data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def inertLast(self,value):
        new_node = node(value)
        if self.start == None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next !=None:
                temp = temp.next
            temp.next = new_node
    def viewList(self):
        if self.start ==None:
            print("Empty")
        else:
            temp = self.start
            while temp!= None:
                print(temp.data,end=' ')
                temp = temp.next

    def search_data(self,item):
        if self.start == None:
            print("Empty linked list")
        else:
            temp = self.start
            while temp !=None:
                if temp.data == item:
                    print('found')
                    break
                temp = temp.next
            else:
                print('not found')





mylist=LinkedList()
mylist.inertLast(10)
mylist.inertLast(21)
mylist.inertLast(31)
mylist.inertLast(41)
mylist.viewList()
print()
mylist.search_data(10)
