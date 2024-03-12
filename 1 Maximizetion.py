#1. Wyndor Glass CO.

# Max : z= 3X_1 +5X_2
#S.t 
# X_1 <= 4
# 2X_2 <= 12
# 3x_1+2X_2 <= 18
# X_1 and X_2 >=0

# Model in Python 
from pulp import *

# Defining the name of the model 

prob = LpProblem("WYNDOR_GLASS_CO.", LpMaximize)
x1 = LpVariable("x_1", lowBound = 0)
x2 = LpVariable("x_2", lowBound = 0)

# Objective function
prob += 3*x1 +5*x2, "Obj"

# Constrains 
prob += x1 <=4
prob += 2*x2 <= 12
prob += 3*x1 + 2*x2 <= 18
print(prob)

prob.solve()
print(f"status: {LpStatus[prob.status]}")
for variable in prob.variables():
    print("{}* = {}". format(variable.name, variable.varValue))
print(value(prob.objective))