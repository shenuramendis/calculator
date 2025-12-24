import operations as op

number = ['0','1','2','3','4','5','6','7','8','9','.']

symbol = {'+': (op.add, 0, 'L', 2),
          '-': (op.subtract, 0, 'L', 2),
          '*' : (op.multiply, 1, 'L', 2),
          '/':(op.divide, 1, 'L', 2),
          'Uminus':(op.uminus, 2, 'R', 1),
          '^':(op.power, 3, 'R', 2)
        }

if __name__ == "__main__":
    pass