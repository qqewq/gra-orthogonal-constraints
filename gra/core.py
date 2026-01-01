class GRA:
    def __init__(self, objective, constraints, lambdas):
        self.objective = objective
        self.constraints = constraints
        self.lambdas = lambdas

    def loss(self, x):
        base = self.objective(x)
        aux = sum(l * c(x) for l, c in zip(self.lambdas, self.constraints))
        return base + aux
