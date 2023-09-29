from z3 import *


def check_validity(sentence):
    
    print(sentence)
    
    s = Solver()
    s.add(sentence)
    result = s.check()  
    if result == sat :
        print("This is satisfiable. A model is:")
        print(s.model() [D])
    elif result == unsat :
        print("This is valid")
    else :
        print("Unable to Solve")


D= DeclareSort('D')

# x = Const('x', D)
# xn = Const('xn', D)

x, xn = Consts ('x xn', D)

sentence = ForAll([x], ForAll([xn], x == xn))

check_validity(sentence)


# ForAll(x, ForAll(xn, x == xn))
# This is satisfiable. A model is:
# [D!val!0]