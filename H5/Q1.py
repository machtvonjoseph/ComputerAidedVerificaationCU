from z3 import *


T = [[Int("t_"+str(i+1)+str(j+1))for j in range (2) ] for i in range (3)]
D = [[2,1],[3,1],[2,3]]

solver=Solver()

for i in range (3):
    for j in range (2):
        if j == 0:
            solver.add(T[i][j] >= 0)
        else:
            solver.add(T[i][j]>=T[i][j-1]+D[i][j-1])
    solver.add(T[i][1]<=8)
    
for j in range (2):
    for i in range (3):
        for k in range (i+1,3):
            solver.add(Or(T[i][j]>=T[k][j]+D[k][j],T[k][j]>=T[i][j]+D[i][j]))
            
#solve the problem
if solver.check() == sat:
    m = solver.model()
    print("T1 = ",m[T[0][0]],"T2 = ",m[T[0][1]])
    print("T3 = ",m[T[1][0]],"T4 = ",m[T[1][1]])
    print("T5 = ",m[T[2][0]],"T6 = ",m[T[2][1]])