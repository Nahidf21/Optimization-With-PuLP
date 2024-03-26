from pulp import *

# Problem
prob = LpProblem("Maximize_Profit", LpMaximize)

# Decision variables
x1 = LpVariable("x1", lowBound=0, cat='Continuous')
x2 = LpVariable("x2", lowBound=0, cat='Continuous')
y1 = LpVariable("y1", cat='Binary')
y2 = LpVariable("y2", cat='Binary')
z = LpVariable("z", cat='Binary')

# Objective
prob += 10*x1 + 15*x2 - 50000*y1 - 70000*y2

# Constraints
M = 100000  # Big M
prob += x1 * 1/50 + x2 * 1/40 <= 500  # Constraint for Factory 1
prob += x1 * 1/40 + x2 * 1/25 <= 700  # Constraint for Factory 2

prob += x1 <= M*y1
prob += x2 <= M*y2

# Solve
prob.solve()

print(f"status: {LpStatus[prob.status]}")
for variable in prob.variables():
    print("{}* = {}". format(variable.name, variable.varValue))
print(value(prob.objective))
