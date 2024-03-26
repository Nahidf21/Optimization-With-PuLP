# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:02:12 2024

@author: nahid
"""

from pulp import *

# Define the problem
prob = LpProblem("Maximize_Profit", LpMaximize)

# Decision variables
x1 = LpVariable("x1", lowBound=0)  # Units of product 1
x2 = LpVariable("x2", lowBound=0)  # Units of product 2
y1 = LpVariable("y1", cat="Binary")  # Setup for product 1
y2 = LpVariable("y2", cat="Binary")  # Setup for product 2

# Objective function
prob += 10*x1 + 15*x2 - 50000*y1 - 70000*y2

# Constraints
M = 100000  # Large constant for linking production decisions to setup costs
prob += (x1* 1 / 50 + x2* 1 / 40) <= 500, "Factory_1_Capacity"
prob += (x1* 1 / 40 + x2 * 1/ 25) <= 700, "Factory_2_Capacity"
prob += x1 <= M*y1, "Link_x1_y1"
prob += x2 <= M*y2, "Link_x2_y2"

# Solve the problem
prob.solve()

# Output results
print(f"status: {LpStatus[prob.status]}")
for variable in prob.variables():
    print("{}* = {}". format(variable.name, variable.varValue))
print(value(prob.objective))