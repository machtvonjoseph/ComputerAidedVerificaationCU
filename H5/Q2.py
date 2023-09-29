from z3 import *

P = [Bool("p_"+str(i+1)) for i in range (10)]

opt = Optimize()

#Add the constraints
opt.add(Or(P[0],P[1],P[2]))
opt.add(Or(P[1],P[3],P[4]))
opt.add(Or(P[2],P[6],P[7]))
opt.add(Or(P[2],P[4],P[5]))
opt.add(Or(P[5],P[8],P[9]))
opt.add(Or(P[4],P[7],P[8]))
opt.add(Or(P[3],P[4],P[7]))
opt.add(Or(P[4],P[5],P[8]))
opt.add(Or(P[1],P[2],P[4]))
opt.add(Or(P[0],P[3],P[5]))
opt.add(Or(P[1],P[6],P[8]))
opt.add(Or(P[2],P[7],P[9]))
opt.add(Or(P[0],P[6],P[9]))
opt.add(Or(P[2],P[3],P[8]))
opt.add(Or(P[1],P[5],P[7]))


#solve the optimizer
opt.minimize(Sum([If(P[i],1,0) for i in range (10)]))

if opt.check() == sat:
    m = opt.model()
    count=0
    for i in range (10):
        if m[P[i]] == True:
            count+=1
    
    print("The minimum number of pennies is ",count)