from z3 import *

U = DeclareSort('U')

#Create a function of type U , U -> U
f = Function('f', U, U)
g = Function('g', U, U)

#Create 4 constants of type U named w,x,y,z
w = Const('w', U)
x = Const('x', U)
y = Const('y', U)
z = Const('z', U)

solver = Solver()


solver.add(Not(ForAll([w,y,z],Implies(And(g(w)==y, (Or(f(g(w))!=f(y), g(w)==z))),y == z))))

#check for satisfiability
if solver.check() == sat:
    print("It is invalid")
else:
    print("It is valid")

#TODO: Explain the difference