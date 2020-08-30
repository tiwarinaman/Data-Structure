def binary_search(list,data):
    lower = 0
    upper = len(list)-1
    while lower <= upper:
        mid = (lower + upper)//2
        if list[mid] == data:
            print('Found data')
            break
        else:
            if data < list[mid]:
                upper -= 1
            else:
                lower += 1
    else:
        print('Not found')


list = [5,10,15,20,25,30]
binary_search(list,30)

                
