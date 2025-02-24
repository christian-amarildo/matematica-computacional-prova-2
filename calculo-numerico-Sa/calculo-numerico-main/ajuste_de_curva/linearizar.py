def ajustar_valores(X: list, f):
    n = len(X)
    new_values_of_x = []
    for i in range(n):
        new_values_of_x.append(f(X[i]))
    
    return new_values_of_x