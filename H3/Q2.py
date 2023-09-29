from z3 import *

x, y = BitVecs('x y', 16)
sentence = (y ^((x ^ y) & -(If(x<y, BitVecVal(1, 16), BitVecVal(0, 16))))) == If(x<y, x, y)

solver = Solver()
solver.add(Not(sentence))

if solver.check() == unsat:
    print("This is valid")
else:
    print("This is not valid")

#this is valid
