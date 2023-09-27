# Вариант 16
from pulp import *

problem = LpProblem("simplex-method", LpMaximize)

x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)
x3 = LpVariable("x3", lowBound = 0)
x4 = LpVariable("x4", lowBound = 0)
x5 = LpVariable("x5", lowBound = 0)

problem += x1 + 2*x2 + x4 + x5
problem += 2*x1 - x2 - x3 == -1
problem += x2 + x4 == 6
problem += x1 + x2 - x5 == 25

problem.solve()
print(f"Максимальное значение функции: {value(problem.objective)}")
print(f"Оптимальные значения переменных 'х': ")
for i in problem.variables():
    print(f"{i.name} = {value(i)}")
