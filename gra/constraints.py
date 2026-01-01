def minimal_description_length(x):
    return len(str(x)) * 0.01

def invariance_constraint(x, transform):
    return abs(x - transform(x))
