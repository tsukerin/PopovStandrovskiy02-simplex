from pulp import *

problem = LpProblem("simplex-method", LpMaximize)

x1 = LpVariable("x1")
x2 = LpVariable("x2", lowBound = 0)

problem += 3*x1 + 4*x2
problem += 3*x1 + 2*x2 - 6 >= 0
problem += 3*x1 - 2*x2 + 7 >= 0
problem += 2*x1 - 4*x2 - 8 <= 0
problem += x1 - 1 >= 0

problem.solve()
print(f"Максимальное значение функции: {value(problem.objective)}")
print(f"Оптимальные значения переменных 'х': ")
for i in problem.variables():
    print(f"{i.name} = {value(i)}")

