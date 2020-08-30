from stack import *
def is_match(p1,p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_expresion_balanced(expresion):
    s = stack()
    is_balanced = True
    index = 0

    while index < len(expresion) and is_balanced:
        exp = expresion[index]
        if exp in "({[":
            s.push(exp)
        else:
            if s.isEmpty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top,exp):
                    return False
        index += 1

    if s.isEmpty() and is_balanced:
        return True
    else:
        return False

print(is_expresion_balanced("(((({}))))"))
print(is_expresion_balanced("([{}]"))


