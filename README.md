# Calculator

This is a simple calculator built in Python 3.14, which first converts the user input (infix) to a Reverse Polish Notation (RPN) expression. 

The expression is converted using a shunting-yard algorithm and is then evaluated.

## Operations

The program currently supports the following operations and functions, which can be found in [operations.py](rpn_calc/operations.py)
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exponentiation (^)
6. Unary minus (~)
7. Factorials and/or Gamma (!)
8. sine
9. cosine
10. tangent

The calculator is also able to detect instances of implicit multiplication.

## Running the program

To run the program, download [run.py](run.py), [exp.txt](exp.txt), and the [rpn_calc](rpn_calc/) folder. 
Edit [exp.txt](exp.txt) to contain your expressions as instructed. 
Run [run.py](test.py) in the terminal.
An output file called "equals.txt" should be created in the same folder as your run.py.
