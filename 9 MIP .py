# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 00:12:52 2024

@author: nahid
"""

from pulp import *

# Define the problem
prob = LpProblem("Minimize_Costs", LpMinimize)

# Decision variables
x_EM = pulp.LpVariable("x_EM", lowBound=0, cat='Integer')
x_EO = pulp.LpVariable("x_EO", lowBound=0, cat='Integer')
x_ET = pulp.LpVariable("x_ET", lowBound=0, cat='Integer')
x_CM = pulp.LpVariable("x_CM", lowBound=0, cat='Integer')
x_CO = pulp.LpVariable("x_CO", lowBound=0, cat='Integer')
x_CT = pulp.LpVariable("x_CT", lowBound=0, cat='Integer')

# Objective function
prob += 260*x_EM + 220*x_EO + 290*x_ET + 220*x_CM + 240*x_CO + 320*x_CT

# Constraints
# Supply constraints
prob += x_EM + x_EO + x_ET <= 20, "Eustis_Supply"
prob += x_CM + x_CO + x_CT <= 20, "Clermont_Supply"

# Demand constraints
prob += x_EM + x_CM == 10, "Miami_Demand"
prob += x_EO + x_CO == 15, "Orlando_Demand"
prob += x_ET + x_CT == 10, "Tallahassee_Demand"

# Solve the model
prob.solve()

print(f"status: {LpStatus[prob.status]}")
for variable in prob.variables():
    print("{}* = {}". format(variable.name, variable.varValue))
print(value(prob.objective))

