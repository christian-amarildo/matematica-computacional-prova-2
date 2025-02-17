import numpy as np
import matplotlib.pyplot as plt
from resolver_sistema_linear import resolver_sistema_linear

def sistema_vandermonde(x, y):
    """
    Constrói a matriz de Vandermonde associada a um conjunto de pontos (x, y).
    
    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    y (list ou array): Lista de valores da variável dependente.
    
    Retorna:
    tuple: (A, b), onde A é a matriz de Vandermonde e b é o vetor de resultados.
    """
    n = len(x)
    A = np.vander(x, increasing=True)  # Usa a função np.vander para simplificar
    return A, np.array(y)

def verificar_solucao(x, fx, coeficientes, exibir_detalhes=False):
    """
    Verifica se os coeficientes encontrados satisfazem as equações do sistema.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    fx (list ou array): Lista de valores da variável dependente.
    coeficientes (np.array): Coeficientes do polinômio encontrados pela solução do sistema.
    exibir_detalhes (bool): Se True, exibe os valores calculados e os erros.

    Retorna:
    bool: True se a solução for válida, False caso contrário.
    """
    estimados = [sum(coef * (xi ** i) for i, coef in enumerate(coeficientes)) for xi in x]
    erros = np.abs(np.array(estimados) - np.array(fx))

    if exibir_detalhes:
        print("\n=== Verificação da Solução ===")
        print("Polinômio encontrado:")
        termos = [f"{coef:.6f} * x^{i}" for i, coef in enumerate(coeficientes)]
        print("P(x) =", " + ".join(termos))
        
        print("\nComparação dos pontos:")
        for xi, yi, yi_est, erro in zip(x, fx, estimados, erros):
            print(f"x = {xi:.6f} | f(x) real = {yi:.6f} | f(x) estimado = {yi_est:.6f} | Erro = {erro:.6e}")

    return np.all(erros < 1e-6)

def resolver_sistema(x, fx, exibir_detalhes=False):
    """
    Resolve o sistema linear Ax = b para encontrar os coeficientes do polinômio interpolador.
    
    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    fx (list ou array): Lista de valores da variável dependente.
    exibir_detalhes (bool): Se True, exibe detalhes da verificação.

    Retorna:
    dict: Dicionário contendo a matriz A, vetor b, coeficientes e resultado do teste de validação.
    """
    A, b = sistema_vandermonde(x, fx)
    coeficientes = resolver_sistema_linear(A, b)
    solucao_valida = verificar_solucao(x, fx, coeficientes, exibir_detalhes)

    return {
        "Matriz A": A,
        "Vetor b": b,
        "Coeficientes": coeficientes,
        "Solução Válida": solucao_valida
    }

def expandir_lista(lista, num_novos):
    """
    Expande uma lista adicionando valores igualmente espaçados entre os valores originais.

    Parâmetros:
    lista (list ou array): Lista de valores numéricos ordenados.
    num_novos (int): Número de novos valores a serem inseridos entre cada par de valores da lista original.

    Retorna:
    list: Nova lista com os valores originais e os novos valores interpolados.
    """
    if len(lista) < 2 or num_novos < 1:
        return lista

    nova_lista = []
    
    for i in range(len(lista) - 1):
        nova_lista.append(lista[i])
        novos_pontos = np.linspace(lista[i], lista[i+1], num_novos + 2)[1:-1]
        nova_lista.extend(novos_pontos)

    nova_lista.append(lista[-1])
    return nova_lista

def plotar_polinomio(x, fx, coeficientes, num_pontos=100):
    """
    Plota o polinômio interpolador junto com os pontos fornecidos.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente.
    fx (list ou array): Lista de valores da variável dependente.
    coeficientes (np.array): Coeficientes do polinômio interpolador.
    num_pontos (int): Número de pontos para a curva interpolada.
    """
    x_range = expandir_lista(x, num_pontos)
    y_range = [sum(coef * (xi ** i) for i, coef in enumerate(coeficientes)) for xi in x_range]

    plt.figure(figsize=(8, 6))
    plt.plot(x_range, y_range, color='darkblue', label="Polinômio Interpolador")
    plt.scatter(x, fx, color='red', marker='o', label="Pontos Originais (f(x))")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Interpolação Polinomial")
    plt.legend()
    plt.grid(True)
    plt.show()

# Testes
x_teste = [-1, 0, 1, 2]
fx_teste = [4, 1, -1, 7]

resultado_teste = resolver_sistema(x_teste, fx_teste, exibir_detalhes=True)
plotar_polinomio(x_teste, fx_teste, resultado_teste["Coeficientes"])

print(resultado_teste)
