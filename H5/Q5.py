from z3 import *

x= Int('x')

f = Function('f', IntSort(), IntSort())

solver = Solver()

#0 < x ∧ x < 3 ∧ f(x) != f(1) ∧ f(x) != f(2)
solver.add(And(0 < x, x < 3, f(x) != f(1), f(x) != f(2)))

if solver.check() == sat:
    print("It is satisfiable")
else:
    print("It is unsatisfiable")
    
    