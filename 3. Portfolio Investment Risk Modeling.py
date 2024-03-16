# Portfolio Investment Risk Modeling 
# Call pulp libray
from pulp import * 
prob = LpProblem("My LP Problem", LpMinimize)


# objective Variables 

x1= LpVariable("Cisco", lowBound= 0, upBound= 200)
x2= LpVariable("Microsoft", lowBound= 0, upBound= 200)
x3= LpVariable("Intel", lowBound= 0, upBound= 200)
x4= LpVariable("BofA", lowBound= 0, upBound= 200)
x5= LpVariable("FirstBank", lowBound= 0, upBound= 200)
x6= LpVariable("ING", lowBound= 50, upBound= 200)
  
# objective function 

prob += 14.2*x1 + 10.57*x2 + 13.22 * x3 + (9.36 ) * x4 + (7.61 ) *x5 + (2.39+ .92) *x6, "Obj"

# Constraints

prob += x1 + x2 + x3 + x4 + x5 + x6 == 500, "Portfolio"
prob += .08*x1 + .06*x2 + .05* x3 + .07 *x4 + .04*x5 + .02* x6 >= 25, "Return"
prob += x4 + x5 >= x1+ x2 + x3, "Balance"

print(prob)

prob.solve()

print("Status:" + LpStatus[prob.status])

for variable in prob.variables():
    print("{}* = {}".format(variable.name, variable.varValue))
    
print(value(prob.objective))

# Sencitivity Analysis 

print("\n Sensitivity Analysis")

for name, c in prob.constraints.items():
    print("\n", name, ":", "slack=", c.slack, " ,Shadow Price =", c.pi)
    
for v in prob.variables():
    print("\n", v.name, "=", v.varValue, ", Reduced Cost = ", v.dj)