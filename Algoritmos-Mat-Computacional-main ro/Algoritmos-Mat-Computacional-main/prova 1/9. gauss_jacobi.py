# V

def gauss_jacobi(A, b, e, max_i):
    n = len(b)
    x = [0.0] * n
    x_novo = [0.0] * n

    for k in range(max_i):
        for i in range(n):
            soma = b[i]

            for j in range(n):
                if i != j:
                    soma -= A[i][j] * x[j]
            x_novo[i] = soma/A[i][i]

        e_total = 0.0
        for i in range(n):
            e_total += abs(x_novo[i] - x[i])

        if e_total < e:
            return x_novo
        
        x = x_novo[:]

    print("Número máximo de iterações atingido:", max_i)
    return x_novo

# Exemplo:
A = [[10, 2, 1],
     [1, 5, 1],
     [2, 3, 10]]

b = [7, -8, 6]
e = 1e-6
max_i = 100

resultado = gauss_jacobi(A, b, e, max_i)
print("Solução:", resultado)
