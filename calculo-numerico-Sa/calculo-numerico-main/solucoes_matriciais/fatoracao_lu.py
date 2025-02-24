def gauss(A: list, b: list):
    n = len(b) - 1
    x = []
    for i in range(n + 1):
        x.append(None)
    
    x[n] = b[n] / A[n][n]
    for k in range(n, -1, -1):
        s = 0
        for j in range(k + 1, n + 1):
            s += A[k][j] * x[j]
        x[k] = (b[k] - s) / A[k][k]
    return x


def print_matriz(Matriz: list, comentario: str):
    print(comentario)
    for i in range(len(Matriz)):
        print(Matriz[i])


def identity(N):
    I = [None] * N
    for j in range(N):
        I[j] = [None] * N
        for k in range(N):
            I[j][k] = 0
        I[j][j] = 1
    return I


def lu(A: list):
    n = len(A)
    p = identity(n)

    for k in range(n):
        pivot = abs(A[k][k])
        r = k
        
        for i in range(k + 1, n):
            if abs(A[i][k]) > pivot:
                pivot = abs(A[i][k])
                r = i
        
        if pivot == 0:
            raise "A MATRIZ É SINGULAR"
        
        if r != k:
            aux = p[k]
            p[k] = p[r]
            p[r] = aux
            for j in range(n):
                aux = A[k][j]
                A[k][j] = A[r][j]
                A[r][j] = aux

        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]
            A[i][k] = m
            for j in range(k + 1, n):
                A[i][j] -= m * A[k][j]

    return A, p


def resolucao_Pb(p: list, b: list):
    n = len(p)
    Pb = []
    for i in range(n):
        line = 0
        for j in range(n):
            line += p[i][j] * b[j]
        Pb.append(line)
    return Pb


def resolucao_y(Lower, Pb):
    n = len(Lower)
    y = [0] * n
    for i in range(n):
        line = Pb[i]
        for j in range(i):
            line -= Lower[i][j] * y[j]
        y[i] = line
    return y


def divide_matriz(A: list):
    n = len(A)
    Upper = A
    Lower = identity(n)
    for i in range(n):
        for j in range(n):
            if i > j:
                Lower[i][j] = A[i][j]
                Upper[i][j] = 0
    return Upper, Lower


def resolver_sistema_lu(A: list, b: list):
    # 1. Fatoração LU com pivoteamento
    A_fatorada, p = lu(A)
    
    # 2. Divide a matriz fatorada em L e U
    Upper, Lower = divide_matriz(A_fatorada)
    
    # 3. Resolve Pb
    Pb = resolucao_Pb(p, b)
    
    # 4. Resolve Ly = Pb
    y = resolucao_y(Lower, Pb)
    
    # 5. Resolve Ux = y
    x = gauss(Upper, y)
    
    return x
