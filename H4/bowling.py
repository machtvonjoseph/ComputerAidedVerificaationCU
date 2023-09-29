from z3 import *


s = Solver()
s.from_file('bowling.dimacs')


s.check()
print(s.model())
