# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 02:49:12 2024

@author: nahid
"""

from pulp import *

# Defining the name of the model 

prob = LpProblem("Maximizetion.", LpMaximize)
x1 = LpVariable("x_1", lowBound = 0)
x2 = LpVariable("x_2", lowBound = 0)

# Objective function
prob += 50*x1 +40*x2, "Obj"

# Constrains 
prob += 3*x1 + x2 <=120 # Working Hours 
prob += 2*x1 + 4*x2 <= 100 # Working Hours 
prob += x1 <= 50 # Units limit 
print(prob)

prob.solve()
print(f"status: {LpStatus[prob.status]}")
for variable in prob.variables():
    print("{}* = {}". format(variable.name, variable.varValue))
print(value(prob.objective))

print("\n Sensitivity Analysis")

for name, c in prob.constraints.items():
    print("\n", name, ":", "slack=", c.slack, " ,Shadow Price =", c.pi)
    
