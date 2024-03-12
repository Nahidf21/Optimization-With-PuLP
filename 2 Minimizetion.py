# Min: z= 3x_1 + 2x_2
#s.t.
# x_1 >= 2
# 2x_1 + x_2 >= 6
# x_1 and x_2 >=0

# MOdel in Python 
from pulp import *
# Defining The model 
prob = LpProblem("Production Cost", LpMinimize)
x1 = LpVariable('x_1', lowBound=0)
x2 = LpVariable("x_2", lowBound=0)
# Objective Function 
prob += 3*x1 +2*x2
#constraints 
prob +=x1 >=2
prob += 2*x1+x2 >=6
print(prob)

prob.solve()
print("Status: " + LpStatus[prob.status])

for variable in prob.variables():
    print("{}* = {}".format(variable.name, variable.varValue))
    
print(value(prob.objective))