def hanoi(n,sr,dest,temp):
    if n>=1:
        hanoi(n-1,sr,temp,dest)
        print('Moved from ',sr, ' to',dest)
        hanoi(n-1,temp,dest,sr)

hanoi(3,1,3,2)
