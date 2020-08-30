class Queue:
    def __init__(self):
        self.qlist = list()
        self.front = None
    def Insert(self,item):
        self.qlist.append(item)
    def delete(self,data):
        self.qlist.remove(data)

q = Queue()
q.Insert(10)
q.Insert(30)
q.Insert(25)
print('Elements in the queuse is :: ',q.qlist)
q.delete(30)
print('After deleting the data from the qlist :: ',q.qlist)
