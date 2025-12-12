import math
import numpy

number_choice = ['0','1','2','3','4','5','6','7','8','9']

def add(a, b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operator_choice = [['+', add, 0],['-',subtract, 0],['*', multiply, 1],['/',divide, 1]]

def result(a,b,operation):
    if operation in [op[0] for op in operator_choice]:
        return operator_choice[([op[0] for op in operator_choice].index(operation))][1](a,b)


def precedence(op):
    out = None
    prec_list = [op[0] for op in operator_choice]
    if op in prec_list:
        out = operator_choice[prec_list.index(op)][2]
    return out

def precedence_check(new_op, old_op): #returns if new operator has a lower precedence than old operator
    out = False
    new_precedence = precedence(new_op)
    old_precedence = precedence(old_op)
    if new_precedence <= old_precedence:
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
            buffer += item
        elif item in [op[0] for op in operator_choice]:
            out.append(buffer)
            buffer = ""
            while (len(operators) > 0) and (precedence_check(item, operators[-1])):
                    out.append(operators.pop())
            operators.append(item)
        elif item == '(':
            operators.append(item)
        elif item == ')':
            while operators[-1] != '(':
                out.append(operators.pop())
            out.append(operators.pop())
    out.append(buffer)
    while len(operators) > 0:
        out.append(operators.pop())
    return out

def calculate(stack):
    out = 0
    buffer_stack = []
    for item in stack:
        if item in [op[0] for op in operator_choice]:
            b = float(buffer_stack.pop())
            a = float(buffer_stack.pop())
            out += result(a,b, item)
            buffer_stack.append(str(out))
        else:
            buffer_stack.append(item)
    return out

def main():
    expression = list(str(input("Enter expression: ")).replace(" ",""))
    rpn_stack = infix(expression)
    print("Result: " + str(calculate(rpn_stack)))

if __name__ == "__main__":
    main()

