import math
import numpy

def main():
    expression = list(str(input("Enter expression: ")).replace(" ",""))
    rpn_stack = infix(expression)
    #print(rpn_stack)
    print("Result: " + str(calculate(rpn_stack)))

if __name__ == "__main__":
    main()

