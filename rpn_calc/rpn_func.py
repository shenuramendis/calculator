import operators as smb

def result(a,b,operation):
    try:
        return smb.symbol[operation][0](a,b)
    except KeyError:
        raise ValueError(f"Unknown operator: {op}")

def precedence(op):
    try:
        return smb.symbol[op][1]
    except KeyError:
        raise ValueError(f"Unknown operator: {op}")
    
def associativity(op):
    try:
        return smb.symbol[op][2]
    except KeyError:
        raise ValueError(f"Unkown operator: {op}")


def precedence_check(new_op, old_op): #returns if new operator has a lower precedence than old operator
    new_precedence = precedence(new_op)
    old_precedence = precedence(old_op)
    if associativity(new_op) == 'L':
        return old_precedence >= new_precedence
    else:
        return old_precedence > new_precedence 

def infix(exp): # reads expression to rpn stack using a shutting-yard algorithm
    if len(exp) == 0:
        return None
    out = [] # return stack
    operators = [] # operator stack while reading
    buffer = ""
    for item in exp:
        if item in smb.number:
            buffer += item
        elif buffer != "":
            out.append(buffer)
            buffer = ""

        if item in smb.symbol.keys():
            while (len(operators) > 0) and (operators[-1] != '(') and precedence_check(item, operators[-1]):
                out.append(operators.pop())
            operators.append(item)
        elif item == '(':
            operators.append(item)
        elif item == ')':
            while (len(operators) >0) and operators[-1] != '(':
                out.append(operators.pop(-1))
            if (len(operators) == 0):
                raise ValueError("Wrong Parentheses")
            operators.pop()
    if buffer != "":
        out.append(buffer)
    while len(operators) > 0:
        if operators[-1] == '(':
            raise ValueError("Wrong Parentheses")
        out.append(operators.pop())
    return out

def calculate(stack):
    buffer_stack = []
    for item in stack:
        if item in smb.symbol.keys():
            b = float(buffer_stack.pop())
            a = float(buffer_stack.pop())
            buffer_stack.append(str(result(a,b,item)))
        else:
            buffer_stack.append(item)
    if len(buffer_stack) != 1:
        raise ValueError("Invalid RPN expression")
    
    return float(buffer_stack[0])

if __name__ == "__main__":
    pass