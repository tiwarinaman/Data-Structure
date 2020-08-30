class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.start = None

    def insertLast(self,value):
        new_node=node(value)
        if self.start==None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next !=None:
                temp = temp.next
            temp.next = new_node

    def deleteFirst(self):
        if self.start == None:
            print('No element present')
        else:
            self.start = self.start.next

    def viewList(self):
        if self.start == None:
            print('List is empty')
        else:
            temp = self.start
            while temp !=None:
                print(temp.data,end=' ')
                temp = temp.next
    

obj =LinkedList()
obj.insertLast(10)
obj.insertLast(20)
obj.insertLast(30)
obj.insertLast(40)
obj.insertLast(50)
print()
obj.viewList()
print()
obj.deleteFirst()
obj.viewList()

