import operations as op

number = ['0','1','2','3','4','5','6','7','8','9','.']

symbol = {'+': (op.add, 0),
          '-': [op.subtract, 0],
          '*' : [op.multiply, 1],
          '/':[op.divide, 1]
        }

if __name__ == "__main__":
    pass