import numpy as np
import matplotlib.pyplot as plt

def construir_matriz_vandermonde(x, funcoes):
    """Constrói a matriz de Vandermonde usando funções base definidas pelo usuário."""
    n = len(x)
    X = np.zeros((n, len(funcoes)))
    for i in range(n):
        for j, f in enumerate(funcoes):
            X[i, j] = f(x[i])
    return X

def resolver_sistema_linear(A, b):
    """Resolve o sistema linear Ax = b usando eliminação de Gauss e substituição regressiva."""
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Eliminação de Gauss
    for i in range(n):
        max_row = np.argmax(np.abs(A[i:, i])) + i
        if A[max_row, i] == 0:
            raise ValueError("Sistema sem solução ou com infinitas soluções.")
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        for j in range(i+1, n):
            fator = A[j, i] / A[i, i]
            A[j, i:] -= fator * A[i, i:]
            b[j] -= fator * b[i]
    
    # Substituição regressiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x

def minimos_quadrados(x, y, funcoes):
    """Implementação do método dos mínimos quadrados usando funções base fornecidas."""
    X = construir_matriz_vandermonde(x, funcoes)
    coeficientes = resolver_sistema_linear(X.T @ X, X.T @ y)
    
    def funcao_ajustada(novo_x):
        return sum(c * f(novo_x) for c, f in zip(coeficientes, funcoes))
    
    return coeficientes, funcao_ajustada

def plot_ajuste(x, y, funcao_final, is_non_linear=False):
    """Plota os pontos fornecidos e a curva ajustada."""
    x_plot = np.linspace(min(x) - 2, max(x) + 2, 200)
    y_plot_ajuste = funcao_final(x_plot)
    
    # Se o ajuste foi feito com transformação, revertemos ao plotar
    if is_non_linear:
        y_plot_ajuste = np.exp(y_plot_ajuste)  # Reverter log se necessário

    plt.scatter(x, y, color='red', label='Pontos Originais')
    plt.plot(x_plot, y_plot_ajuste, color='blue', label='Ajuste Calculado')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ajuste pelo Método dos Mínimos Quadrados')
    plt.legend()
    plt.grid()
    plt.show()

# --- Código principal ---
if __name__ == "__main__":
    # 🔹 Passo 1: Definir os dados de entrada
    x_exemplo = np.array([1, 2, 3, 4, 5])  # Substituir pelos pontos reais
    y_exemplo = np.array([2.718, 1.484, 0.738, 0.367, 0.135])  # Substituir pelos pontos reais

    # 🔹 Passo 2: Verificar se os dados são lineares ou não
    is_non_linear = True  # 🔴 O PROGRAMADOR DEVE ALTERAR ESSA VARIÁVEL! (True para não linear, False para linear)

    # 🔹 Passo 3: Aplicar transformação se for necessário
    if is_non_linear:
        print("🔄 Aplicando transformação logarítmica nos dados para ajuste exponencial...")
        y_exemplo = np.log(y_exemplo)  # Aplicamos log para linearizar se necessário

    # 🔹 Passo 4: Definir as funções base para ajuste
    if is_non_linear:
        funcoes_base = [lambda x: 1, lambda x: x]  # Para modelo exponencial transformado
    else:
        funcoes_base = [lambda x: 1, lambda x: x, lambda x: x**2]  # Para modelo quadrático (exemplo)

    # 🔹 Passo 5: Aplicar o método dos mínimos quadrados
    coef, func_ajustada = minimos_quadrados(x_exemplo, y_exemplo, funcoes_base)

    # 🔹 Passo 6: Reverter transformação se necessário
    if is_non_linear:
        print("🔄 Revertendo transformação ao calcular valores ajustados...")
        def func_ajustada_final(novo_x):
            return np.exp(func_ajustada(novo_x))  # Reverte log(y)

    else:
        func_ajustada_final = func_ajustada

    # 🔹 Passo 7: Plotar os dados e a curva ajustada
    plot_ajuste(x_exemplo, np.exp(y_exemplo) if is_non_linear else y_exemplo, func_ajustada_final, is_non_linear)

    # 🔹 Passo 8: Exibir coeficientes ajustados
    print("Coeficientes ajustados:", coef)

    # 🔹 Passo 9: Testar a função ajustada para novos valores de x
    novos_x = np.array([6, 7, 8])
    novos_y = func_ajustada_final(novos_x)
    print("Novos valores de x:", novos_x)
    print("Valores ajustados de y:", novos_y)
