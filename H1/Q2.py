from z3 import *

#Calcuro Solver

X = [ [ Int("x_%s_%s" % (i+1, j+1)) for j in range(4) ]
      for i in range(4) ]

#each cell contains a value in {0,1,2,3}
cells_c  = [ And(1 <= X[i][j], X[i][j] <= 4) for i in range(4) for j in range(4) ]

#each row contains a digit at most once
rows_c   = [ Distinct(X[i]) for i in range(4) ]
#each column contains a digit at most once
cols_c   = [ Distinct([ X[i][j] for i in range(4) ]) for j in range(4) ]

#first two rows on the first column should have a ratio of 2:1
half_ratio = [Or(X[0][0]/2 == X[1][0], X[0][0] == X[1][0]/2)]

#the 8+ cells
eight_addition = [X[0][1]+X[0][2]+X[1][1] == 8]

#the 6x cells
six_multiplication = [X[2][0]*X[3][0]*X[3][1] == 6]

#the 3- cells
three_subtraction = [Or(X[3][2]-X[3][3] == 3, X[3][3]-X[3][2] == 3)]

#the 24* cells
twentyfour_multiplication = [X[2][2]*X[2][3]*X[1][3] == 24]


calcuro_c = cells_c + half_ratio + eight_addition + \
            six_multiplication + three_subtraction + twentyfour_multiplication\
            + rows_c + cols_c


#calcuro instance (0 means empty cell)
instance = ((0,0,0,1),
            (0,0,2,0),
            (0,3,0,0),
            (0,0,0,0))

instance_c = [ If(instance[i][j] == 0, True, X[i][j] == instance[i][j]) 
              for i in range(4) for j in range(4) ] 

s = Solver()
s.add(calcuro_c + instance_c)
if s.check() == sat:
    m = s.model()
    r = [ [ m.evaluate(X[i][j]) for j in range(4) ]
          for i in range(4) ]
    import numpy as np
    print(np.matrix(r))
else:
    print ("failed to solve")
    
    
#ANSWER INSTANCE:
# [[2 4 3 1]
#  [4 1 2 3]
#  [1 3 4 2]
#  [3 2 1 4]]