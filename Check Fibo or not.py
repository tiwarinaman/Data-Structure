def is_fib(num):
    a , b = 0, 1

    if num == a or num == b :
        print('Fibonacci Number')
    else:
        c = a+b
        while(c<num):
            c=a+b
            a,b=b,c
            if c==num:
                print('Fibonacci Number')
                break
        else:
            print('Not a fibonacci number')

if __name__ == '__main__':
    num = int(input('Enter a number '))
    is_fib(num)
