import math, numpy

operator_choice = [['+','-'],['*','/']]
number_choice = ['0','1','2','3','4','5','6','7','8','9']

def precedence(new_op, old_op): #returns if new operator has a lower precedence than old operator
    out = False
    for item in operator_choice:
        if new_op in item:
            new_precedence = operator_choice.index(item)
        if old_op in item:
            old_precedence = operator_choice.index(item)

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
        if item in number_choice:
            buffer.append(item)
        elif item in operator_choice:
            out.append(buffer)
            buffer = ""
            while (len(operators) > 0) and precedence(item, operators[-1]):
                    out.append(operators.pop())
            operators.append(item)
        elif item == '(':
            operators.append(item)
        elif item == ')':
            while operators[-1] != '(':
                out.append(operators.pop())
            out.append(operators.pop())
    while len(operators) > 0:
        out.append(operators.pop())

def main():
    expression = str(input("Enter expression: ")).replace(" ","").split("")
    rpn_stack = infix(expression)

if __name__ == "__main__":
    main()

