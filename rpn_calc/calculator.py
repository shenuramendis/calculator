import operations as op
import rpn as rpn

def main():
    expression = list(str(input("Enter expression: ")).replace(" ",""))
    rpn_stack = rpn.infix(expression)
    print(rpn_stack)
    print("Result: " + str(rpn.calculate(rpn_stack)))

if __name__ == "__main__":
    main()

