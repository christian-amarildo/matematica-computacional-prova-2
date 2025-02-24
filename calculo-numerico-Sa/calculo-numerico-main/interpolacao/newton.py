# USAR INTERPOLAÇÃO SOMENTE PARA VALORES DENTRO DO INTERVALO DE X
def create_empty_triangular_matrix(Y: list, n: int) -> list:
    triangular_matrix = []
    for i in range(n, 0, -1):
        line = [None] * i
        triangular_matrix.append(line)
    
    for line in range(n):
        line_len = len(triangular_matrix[line])
        for col in range(line_len):
            if col == 0:
                triangular_matrix[line][col] = Y[line]
    
    return triangular_matrix


def newton_coeficients(X: list, Y: list):
    n = len(X)

    coefs = create_empty_triangular_matrix(Y, n)
    for col in range(1, n):
        count = 0
        for line in range(n-1):
            if coefs[0][-1] != None:
                break

            num = coefs[line+1][col-1] - coefs[line][col-1] # first line
            a = X[col+count]
            b = X[line]
            den = a-b
            d = num/den
            coefs[line][col] = d
            count += 1
    
    return coefs


def newton(x: int, coef_in_first_line: list, X: list):
    n = len(coef_in_first_line)
    result = coef_in_first_line[0]
    coef = 1

    for i in range(1, n):
        coef *= x - X[i-1]
        result += coef_in_first_line[i] * coef
    
    return result
