# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:53:28 2024

@author: nahid
"""

from pulp import *

# Problem
prob = pulp.LpProblem("Household_Tasks_Minimization", LpMinimize)

# Decision Variables
x_ES = LpVariable('x_Eve_Shopping', cat='Binary')
x_EC = LpVariable('x_Eve_Cooking', cat='Binary')
x_ED = LpVariable('x_Eve_Dishwashing', cat='Binary')
x_EL = LpVariable('x_Eve_Laundry', cat='Binary')

x_SS = LpVariable('x_Steven_Shopping', cat='Binary')
x_SC = LpVariable('x_Steven_Cooking', cat='Binary')
x_SD = LpVariable('x_Steven_Dishwashing', cat='Binary')
x_SL = LpVariable('x_Steven_Laundry', cat='Binary')

# Objective Function
prob += 4.5 * x_ES + 7.5 * x_EC + 3.5 * x_ED + 3.0 * x_EL + \
         5.0 * x_SS + 7.2 * x_SC + 4.5 * x_SD + 3.2 * x_SL

# Constraints
# Each task is assigned exactly once
prob += x_ES + x_SS == 1
prob += x_EC + x_SC == 1
prob += x_ED + x_SD == 1
prob += x_EL + x_SL == 1

# Each person is assigned exactly two tasks
prob += x_ES + x_EC + x_ED + x_EL == 2
prob += x_SS + x_SC + x_SD + x_SL == 2

# Solve
prob.solve()

print(f"status: {LpStatus[prob.status]}")
for variable in prob.variables():
    print("{}* = {}". format(variable.name, variable.varValue))
print(value(prob.objective))
