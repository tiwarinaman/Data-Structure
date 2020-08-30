#Defining a list for the heap
data = [0,20,25,35,60,42]

#Define a function
def minHeapInsert(item):
    #Find the length of the list and send position as the last index
    #Because when the data is inserted in the heap that is inserted
    # At the last so we take the index of the list
    pos = len(data)

    #Inserting the data at the last position
    #After inserting the data your list will become
    # [0,20,25,35,60,42,92]
    data.insert(pos,item)
    
    print('After inserting the data in heap')
    print(data) # Here we are just printing the list after inserting the value

    # Here we are just checking whether my position is 0 or not if not that
    # Means we have some data and we have to arrange and put the newly added
    # Data at the right place
    if pos!=0:

        # Here we are checking, so you know that we are working with the minimum
        # heap so the concept is my parent node should be less than the child node
        # I know you are aware about that[Smile on your face...hahaha.]
        # So, I know in your mind the question will come that how can we find the paraent
        # node of any child so the logic is [i+1/2] or i//2 this is the logic
        # Whether the i is the index number so, now come onto the loop condition
        # We are giving the condition that hey loop run unlit my paraent is grater than the newly
        # added data. Because we have to make the paraent small.
        while data[pos//2 >= item and pos//2 >= 1]:
            
            # Now we are just swaping data.
            # Now you will track what is happening...hahaha.
            data[pos] = data[pos//2]
            data[pos//2] = item

            # printing the list after find the right position of the newly added data.
            print(data)

            # Just checking all the time what is the paraent value is.
            pos = pos//2

# Printing the initial list that we have defined above.
print('Heap in array format')
print(data)
#Calling the function
minHeapInsert(92)

# That's It.......

