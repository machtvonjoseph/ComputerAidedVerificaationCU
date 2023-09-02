from z3 import *

A = DeclareSort('A')
x, y = Consts('x y', A)

f = Function('+', A, A, A)
zero = Const('0', A)

s=Solver()
s.add(Exists([y], ForAll([x], f(x,y) == zero)))
print (s.check())

#This is satisfiable



