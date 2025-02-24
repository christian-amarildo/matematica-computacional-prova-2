def norma(v):
    return sum(vi**2 for vi in v) ** 0.5

def resolver_sistema_linear(A, b):
    n = len(A)
    x = [0] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            b[j] -= fator * b[i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]

    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - soma) / A[i][i]
    
    return x

def newton_modificado(F, J, x0, epsilon1, epsilon2, max_iter=100):
    x_k = x0[:]  
    J_k = J(x_k)  
    
    for k in range(max_iter):
        F_k = F(x_k)

        if norma(F_k) < epsilon1:
            return x_k, k, True

        try:
            s_k = resolver_sistema_linear([row[:] for row in J_k], [-fi for fi in F_k])
        except ZeroDivisionError:
            return x_k, k, False  
        
        x_k_plus_1 = [x_k[i] + s_k[i] for i in range(len(x_k))]

        if norma([x_k_plus_1[i] - x_k[i] for i in range(len(x_k))]) < epsilon2:
            return x_k_plus_1, k + 1, True

        x_k = x_k_plus_1

        if k % 5 == 0:  
            J_k = J(x_k)

    return x_k, max_iter, False  
