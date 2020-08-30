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

def infixToPostfix(s):
    pr = {}
    pr['*'] = 3
    pr['/'] = 3
    pr['+'] = 2
    pr['-'] = 2
    pr['('] = 1

    opstack = stack()
    postfix = []
    for token in s:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfix.append(topToken)
                topToken = opstack.pop()
        else:
            while not opstack.isEmpty() and pr[opstack.peek()] >= pr[token]:
                postfix.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postfix.append(opstack.pop())
    return " ".join(postfix)
print(infixToPostfix('A+B'))
print(infixToPostfix('(A+B)*C'))

