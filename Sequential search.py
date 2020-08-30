def binary_search(list,data):
    for i in list:
        if i==data:
            print("Data is present")
            break
    else:
        print("Not found")

list=[32,33,41,35,67,54,3,5,44,3,2]
data = int(input('What you want to search :: '))
binary_search(list,data)


              
