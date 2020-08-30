data = [0,85,75,60,30,35,45]
def maxHeapInsert(item):
    pos = len(data)
    data.insert(pos,item)
    print('After inserting the element in the heap')
    print(data)
    if pos!=0:
        while data[int(pos/2) <= item and int(pos/2) >=1]:
            data[pos] = data[int(pos/2)]
            data[int(pos/2)] = item
            print(data)
            pos = int(pos/2)

print('Heap format in array ')
print(data)
maxHeapInsert(92)
