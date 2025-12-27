import operations as op
import math

number = ['0','1','2','3','4','5','6','7','8','9','.']

constant = {
            'e': math.e,
            'π': math.pi,
           }

class sym_func:
    
    def __init__(self, function, arity, associativity='x', precedence='-1'):
        self.function = function
        self.precedence = precedence
        self.associativity = associativity
        self.arity = arity

symbol = {
          '+': sym_func(op.add, 2, 'L', 0),
          '-': sym_func(op.subtract, 2, 'L', 0),
          '*' : sym_func(op.multiply, 2, 'L', 1),
          '/': sym_func(op.divide, 2, 'L', 1),
          '~': sym_func(op.uminus, 1, 'R', 2),
          '^': sym_func(op.power, 2, 'R', 3),
          '!': sym_func(op.fact, 1, 'R', 4)
         }

function = {
            'sin': sym_func(op.sine,1),
            'cos': sym_func(op.cosine,1),
            'tan': sym_func(op.tangent,1),
           }



if __name__ == "__main__":
    pass