from gra.core import GRA
from gra.optimizer import optimize

def objective(x):
    return (x**2 - 1)**2

def stabilizer(x):
    return abs(x)

gra = GRA(objective, [stabilizer], [0.1])
solution = optimize(gra, x0=2.0)

print("Collapsed solution:", solution)
