from z3 import *

U = DeclareSort('U')

#Create a function of type U , U -> U
f = Function('f', U, U)

#Create 4 constants of type U named w,x,y,z
w = Const('w', U)
x = Const('x', U)
y = Const('y', U)
z = Const('z', U)

solver = Solver()


solver.add(Not(ForAll([x,z,w],Implies(And(f(x) == z, f(z) == w,x == z),w == x))))

#check for satisfiability
if solver.check() == sat:
    print("It is invalid")
else:
    print("It is valid")
