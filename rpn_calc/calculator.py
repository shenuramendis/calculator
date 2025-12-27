import sys
import operations as op
import rpn_func as rpn

#for debugging only
'''
def main():
    expression = rpn.token(input())
    print(expression)
    rpn_stack = rpn.postfix(expression)
    print(rpn_stack)
    print(str(rpn.calculate(rpn_stack)))
'''

def main():
    if len(sys.argv) == 2:
        expression = rpn.token(sys.argv[1])
        rpn_stack = rpn.postfix(expression)
        print(str(rpn.calculate(rpn_stack)))
    elif len(sys.argv) > 2:
        raise TypeError("Only one expression at a time")
    else:
        raise TypeError("Missing expression")


if __name__ == "__main__":
    main()

