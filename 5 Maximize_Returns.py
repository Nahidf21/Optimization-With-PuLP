# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 17:39:43 2024

@author: nahid
"""

# MOdel in Python 
from pulp import *
# Defining The model 
prob = LpProblem("Minimization", LpMinimize)
x1 = LpVariable('x_1', lowBound=0)
x2 = LpVariable("x_2", lowBound=0)
x3 = LpVariable("x_3", lowBound=0)
# Objective Function 
prob += 3*x1 +4*x2 + 5*x3
#constraints 
prob += 2*x2 + x3 >= 8
prob += x2 + x3 >= 6
prob += 6*x1 + 8*x2 >= 48

print(prob)

prob.solve()
print("Status: " + LpStatus[prob.status])

for variable in prob.variables():
    print("{}* = {}".format(variable.name, variable.varValue))
    
print(value(prob.objective))

print("\n Sensitivity Analysis")

for name, c in prob.constraints.items():
    print("\n", name, ":", "slack=", c.slack, " ,Shadow Price =", c.pi)
    
for v in prob.variables():
    print("\n", v.name, "=", v.varValue, ", Reduced Cost = ", v.dj)