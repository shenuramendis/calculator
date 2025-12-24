import sys
import operations as op
import rpn_func as rpn

def main():
    if len(sys.argv) == 2:
        expression = list(sys.argv[1].replace(" ",""))
        rpn_stack = rpn.infix(expression)
        #print(rpn_stack)
        print(str(rpn.calculate(rpn_stack)))
    elif len(sys.argv) > 2:
        raise TypeError("Only one expression at a time")
    else:
        raise TypeError("Missing expression")

if __name__ == "__main__":
    main()

