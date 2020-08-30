def mearge_sort(list):
    if len(list) > 1:
        mid = len(list)//2
        left_half = list[:mid]
        right_half = list[mid:]
        mearge_sort(left_half)
        mearge_sort(right_half)
        i=j=k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list[k] = left_half[i]
                i+=1
            else:
                list[k] = right_half[j]
                j+=1
            k+=1
        while i<len(left_half):
            list[k] = left_half[i]
            i+=1
            k+=1
        while j<len(right_half):
            list[k] = right_half[j]
            j+=1
            k+1


list = [32,21,0,9,5,34]
mearge_sort(list)
print(list)
