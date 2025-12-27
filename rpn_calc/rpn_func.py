from operators import symbol as smb
from operators import constant as const
from operators import function as func
from operators import number as num
def result(a,b,operation, type):
    try:
        if type == "smb":
            return smb[operation].function(a,b)
        elif type == "func":
            return func[operation].function(a,b)
    except KeyError:
        raise ValueError(f"Unknown operator: {operation}")

def precedence(op):
    try:
        return smb[op].precedence
    except KeyError:
        raise ValueError(f"Unknown operator: {op}")
    
def associativity(op):
    try:
        return smb[op].associativity
    except KeyError:
        raise ValueError(f"Unkown operator: {op}")


def precedence_check(new_op, old_op): #returns if new operator has a lower precedence than old operator
    if new_op == '~':
        return False
    new_precedence = precedence(new_op)
    old_precedence = precedence(old_op)
    if associativity(new_op) == 'L':
        return old_precedence >= new_precedence
    else:
        return old_precedence > new_precedence 
    
def unary_minus(input):
    string = ""
    for n in range(len(input)):
        if input[n] == '-':
            if n == 0:
                string = string + '~'
            elif n > 0:
                if input[n-1] in smb.keys() or input[n-1] == '(':
                    string = string + '~'
                else:
                    string = string + '-'
        else:
            string = string + input[n]
    return string

def token(string):
    out = string.replace(" ", "")
    out = string.replace("Ï€", "π")
    out = unary_minus(out)
    exp = []
    buffer = ''
    n = 0
    i = 0
    for n in range(len(out)):
        if out[n] in num:
            if out[n] == '.' and out[n] in buffer:
                raise ValueError("Floating point number cannot have more than one decimal point.") 
            buffer += out[n]
        elif out[n] in const.keys():
            exp.append(out[n])
        elif out[n] in smb.keys():
            if buffer != "":
                exp.append(buffer)
                buffer = ""
            exp.append(out[n])
        elif out[n].isalpha():
            if n >= i:
                if buffer != "":
                    exp.append(buffer)
                    buffer = ""
                add = ""
                i = n
                while i < len(out) and out[i].isalpha():
                    add += out[i]
                    i += 1
                exp.append(add)
        elif out[n] in '()':
            if buffer != "":
                exp.append(buffer)
                buffer = ""
            exp.append(out[n])
        else:
            raise ValueError("Invalid character")
    if buffer != "":
        exp.append(buffer)
    return exp

def implicit_multiplication(exp):
    out = exp.copy()
    n = 1
    while n < len(out):
        if (out[n] == '(' or out[n] in func.keys())and (any(c.isdigit() for c in str(out[n-1])) or out[n-1] in ')!' ):
            out.insert(n, '*')
            n += 1
        n += 1
    return out       
   
def replace_constants(exp):
    out = exp.copy()
    for n in range(len(out)):
        if out[n] in const.keys():
            out[n] = const[out[n]]
    return out

def postfix(exp): # reads expression to rpn stack using a shunting-yard algorithm
    if len(exp) == 0:
        return None
    out = [] # return stack
    operators = [] # operator stack while reading
    check = replace_constants(implicit_multiplication(exp))
    for item in check:
        if any(c.isdigit() for c in str(item)):
            out.append(item)

        elif item in smb.keys():
            while (len(operators) > 0) and (operators[-1] != '(') and (operators[-1] in smb .keys()) and precedence_check(item,operators[-1]):
                out.append(operators.pop())
            operators.append(item)

        elif item in func.keys():
            operators.append(item)

        elif item == '(':
            operators.append(item)

        elif item == ')':
            while (len(operators) > 0) and operators[-1] != '(':
                out.append(operators.pop())
            if (len(operators) == 0):
                raise ValueError("Wrong Parentheses")
            operators.pop()
            if (len(operators)>0) and operators[-1] in func.keys():
                out.append(operators.pop())
        
    while len(operators) > 0:
        if operators[-1] == '(':
            raise ValueError("Wrong Parentheses")
        out.append(operators.pop())
    return out

def calculate(stack):
    buffer_stack = []
    for item in stack:
        if item in smb.keys():
            type = "smb"
            if smb[item].arity == 2:
                b = float(buffer_stack.pop())
                a = float(buffer_stack.pop())
            else:
                a = float(buffer_stack.pop())
                b = None
            buffer_stack.append(str(result(a,b,item,type)))
        elif item in func.keys():
            type = "func"
            a = float(buffer_stack.pop())
            b = None
            buffer_stack.append(str(result(a,b,item,type)))
        else:
            buffer_stack.append(item)
    if len(buffer_stack) != 1:
        raise ValueError("Invalid RPN expression")
    
    buffer_stack[0] = round(float(buffer_stack[0]), 10)
    return float(buffer_stack[0])

if __name__ == "__main__":
    pass