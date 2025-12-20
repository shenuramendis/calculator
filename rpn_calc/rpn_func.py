import operators as smb

def result(a,b,operation):
    if operation in smb.symbol.keys():
        return smb.symbol[operation][0](a,b)

def precedence(op):
    out = None
    if op in smb.symbol.keys():
        out = smb.symbol[op][1]
    
    return out

def precedence_check(new_op, old_op): #returns if new operator has a lower precedence than old operator
    out = False
    new_precedence = precedence(new_op)
    old_precedence = precedence(old_op)
    if new_precedence < old_precedence:
        out = True 
    return out

def infix(exp): # reads expression to rpn stack using a shutting-yard algorithm
    if len(exp) == 0:
        return None
    out = [] # return stack
    operators = [] # operator stack while reading
    buffer = ""
    for item in exp:
        if item in smb.number:
            buffer += item
            print(buffer)
        elif item in smb.symbol.keys():
            out.append(buffer)
            buffer = ""
            while (len(operators) > 0) and (operators[-1] != '('):
                if precedence_check(item, operators[-1]):
                    out.append(operators.pop())
            operators.append(item)
        elif item == '(':
            operators.append(item)
        elif item == ')':
            while operators[-1] != '(':
                out.append(operators.pop(-1))
            operators.pop(-1)
    out.append(buffer)
    while len(operators) > 0:
        out.append(operators.pop())
    return out

def calculate(stack):
    out = 0
    buffer_stack = []
    for item in stack:
        if item in smb.symbol.keys():
            buffer_stack.pop()
            b = float(buffer_stack.pop())
            a = float(buffer_stack.pop())
            buffer_stack.append(str(result(a,b,item)))
        else:
            buffer_stack.append(item)
    out = buffer_stack[0]
    return out

if __name__ == "__main__":
    pass