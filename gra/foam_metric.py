def foam_metric(candidates, projector):
    phi = 0.0
    for i in range(len(candidates)):
        for j in range(len(candidates)):
            if i != j:
                phi += abs(projector(candidates[i], candidates[j])) ** 2
    return phi
