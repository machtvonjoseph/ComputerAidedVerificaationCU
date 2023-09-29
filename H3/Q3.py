from z3 import *

S,(a,b,c,d,e) = EnumSort('S', ('a', 'b', 'c', 'd', 'e'))

A = [Function(f"A{i}", S, BoolSort()) for i in range(0, 10)]

s = Solver()

for i in range(0, 10):
    for j in range(0, 10):
        if i != j:
            s.add(Or(
                And(A[i](a), Not(A[j](a))),
                And(A[i](b), Not(A[j](b))),
                And(A[i](c), Not(A[j](c))),
                And(A[i](d), Not(A[j](d))),
                And(A[i](e), Not(A[j](e)))
            ))
         
if s.check() == sat:
    print(s.model())
   

#satisfiable for 10 subsets        
            
#I worked on this problem with a fellow classmate, Gaukas Wang.