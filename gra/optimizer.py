def numerical_grad(f, x, eps=1e-5):
    return (f(x + eps) - f(x - eps)) / (2 * eps)

def optimize(gra, x0, steps=1000, lr=0.01):
    x = x0
    for _ in range(steps):
        grad = numerical_grad(gra.loss, x)
        x -= lr * grad
    return x
