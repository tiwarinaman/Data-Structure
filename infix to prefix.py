class stack:
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return self.item == []
    def push(self,value):
        self.item.insert(0,value)
    def pop(self):
        return self.item.pop(0)
    def peek(self):
        return self.item[0]

def infixToPrefix(s):
    pr = {}
    pr['*'] = 3
    pr['/'] = 3
    pr['+'] = 2
    pr['-'] = 2
    pr['('] = 1
    opstack = stack()
    prefix = []
    temp = []
    for token in s:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            prefix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            topToken = opstack.pop()
            while topToken is not '(':
                temp.append(topToken)
                topToken = opstack.pop()
                prefix = temp + prefix
                temp = []
        else:
            while not opstack.isEmpty() and pr[opstack.peek()] >= pr[token]:
                temp.append(opstack.pop())
            prefix = temp + prefix
            opstack.push(token)
            temp = []
    while not opstack.isEmpty():
        temp.append(opstack.pop())
        prefix = temp + prefix
    return " ".join(prefix)
        
print(infixToPrefix('A+B'))




















