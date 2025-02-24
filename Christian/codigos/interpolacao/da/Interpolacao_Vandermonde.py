import numpy as np  # Importa a biblioteca NumPy para manipulações numéricas
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para gerar gráficos
from resolver_sistema_linear import resolver_sistema_linear  # Importa a função que resolve sistemas lineares (já implementada em outro arquivo)

# Função para construir a matriz de Vandermonde associada a um conjunto de pontos (x, y)
def sistema_vandermonde(x, y):
    """
    Constrói a matriz de Vandermonde associada a um conjunto de pontos (x, y).
    A matriz de Vandermonde é usada para resolver sistemas lineares que surgem na interpolação polinomial.
    
    Parâmetros:
    x (list ou array): Lista de valores da variável independente (x1, x2, ..., xn).
    y (list ou array): Lista de valores da variável dependente (y1, y2, ..., yn), correspondentes a cada valor de x.
    
    Retorna:
    tuple: (A, b), onde:
      - A é a matriz de Vandermonde (de dimensão n x n)
      - b é o vetor de resultados (vetor de valores y)
    """
    n = len(x)  # Obtém o número de pontos fornecidos
    A = np.vander(x, increasing=True)  # Constrói a matriz de Vandermonde. np.vander gera uma matriz com as potências de x, do menor grau para o maior
    return A, np.array(y)  # Retorna a matriz A e o vetor b com os valores de y

# Função para verificar se a solução do sistema satisfaz as equações originais
def verificar_solucao(x, fx, coeficientes, exibir_detalhes=False):
    """
    Verifica se os coeficientes encontrados satisfazem as equações do sistema original.
    Para isso, avalia o polinômio interpolador nos pontos dados e calcula os erros.

    Parâmetros:
    x (list ou array): Lista de valores da variável independente (x1, x2, ..., xn).
    fx (list ou array): Lista de valores da variável dependente (y1, y2, ..., yn).
    coeficientes (np.array): Coeficientes do polinômio interpolador encontrados pela solução do sistema.
    exibir_detalhes (bool): Se True, exibe detalhes da comparação entre o valor real de f(x) e o valor estimado pelo polinômio.
    
    Retorna:
    bool: Retorna True se a solução for válida (os erros são suficientemente pequenos), False caso contrário.
    """
    # Estima os valores de f(x) usando os coeficientes do polinômio para cada valor de x
    estimados = [sum(coef * (xi ** i) for i, coef in enumerate(coeficientes)) for xi in x]
    
    # Calcula o erro absoluto entre os valores reais de f(x) e os valores estimados pelo polinômio
    erros = np.abs(np.array(estimados) - np.array(fx))

    # Se exibir_detalhes for True, exibe o polinômio e a comparação dos valores reais e estimados
    if exibir_detalhes:
        print("\n=== Verificação da Solução ===")
        print("Polinômio encontrado:")
        
        # Exibe o polinômio interpolador com os coeficientes calculados
        termos = [f"{coef:.6f} * x^{i}" for i, coef in enumerate(coeficientes)]
        print("P(x) =", " + ".join(termos))
        
        # Exibe a comparação dos valores reais de f(x) com os valores estimados e o erro
        print("\nComparação dos pontos:")
        for xi, yi, yi_est, erro in zip(x, fx, estimados, erros):
            print(f"x = {xi:.6f} | f(x) real = {yi:.6f} | f(x) estimado = {yi_est:.6f} | Erro = {erro:.6e}")

    # Se todos os erros forem menores que 1e-6, considera a solução válida
    return np.all(erros < 1e-6)

# Função principal para resolver o sistema linear e encontrar os coeficientes do polinômio interpolador
def resolver_sistema(x, fx, exibir_detalhes=False):
    """
    Resolve o sistema linear Ax = b para encontrar os coeficientes do polinômio interpolador.
    
    Parâmetros:
    x (list ou array): Lista de valores da variável independente (x1, x2, ..., xn).
    fx (list ou array): Lista de valores da variável dependente (y1, y2, ..., yn).
    exibir_detalhes (bool): Se True, exibe detalhes da verificação da solução.

    Retorna:
    dict: Dicionário contendo as informações do processo:
      - "Matriz A": Matriz de Vandermonde
      - "Vetor b": Vetor b com os valores de fx
      - "Coeficientes": Coeficientes do polinômio interpolador
      - "Solução Válida": Resultado do teste de validação (True/False)
    """
    # Constrói a matriz A de Vandermonde e o vetor b com os valores de fx
    A, b = sistema_vandermonde(x, fx)
    
    # Resolve o sistema linear Ax = b usando uma função externa (que você deve implementar ou importar)
    coeficientes = resolver_sistema_linear(A, b)
    
    # Verifica se a solução encontrada é válida (os erros estão dentro de uma margem aceitável)
    solucao_valida = verificar_solucao(x, fx, coeficientes, exibir_detalhes)

    # Retorna as informações relevantes como um dicionário
    return {
        "Matriz A": A,
        "Vetor b": b,
        "Coeficientes": coeficientes,
        "Solução Válida": solucao_valida
    }

# Função para expandir uma lista de valores numéricos, inserindo valores intermediários igualmente espaçados
def expandir_lista(lista, num_novos):
    """
    Expande uma lista de valores adicionando pontos igualmente espaçados entre os valores originais.
    
    Parâmetros:
    lista (list ou array): Lista de valores numéricos ordenados.
    num_novos (int): Número de novos valores a serem inseridos entre cada par de valores da lista original.
    
    Retorna:
    list: Nova lista com os valores originais e os novos valores interpolados.
    """
    if len(lista) < 2 or num_novos < 1:
        return lista  # Retorna a lista original se houver menos de dois elementos ou se num_novos for inválido
    
    nova_lista = []  # Inicializa a nova lista com os pontos originais
    
    # Para cada par de valores consecutivos na lista original
    for i in range(len(lista) - 1):
        nova_lista.append(lista[i])  # Adiciona o primeiro valor
        novos_pontos = np.linspace(lista[i], lista[i+1], num_novos + 2)[1:-1]  # Cria pontos igualmente espaçados entre os valores originais
        nova_lista.extend(novos_pontos)  # Adiciona os novos pontos na lista
    
    nova_lista.append(lista[-1])  # Adiciona o último valor original
    return nova_lista

# Função para plotar o gráfico do polinômio interpolador junto com os pontos originais
def plotar_polinomio(x, fx, coeficientes, num_pontos=100):
    """
    Plota o polinômio interpolador junto com os pontos fornecidos.
    
    Parâmetros:
    x (list ou array): Lista de valores da variável independente (x1, x2, ..., xn).
    fx (list ou array): Lista de valores da variável dependente (y1, y2, ..., yn).
    coeficientes (np.array): Coeficientes do polinômio interpolador.
    num_pontos (int): Número de pontos para a curva interpolada. (Quanto maior, mais suave será o gráfico)
    """
    # Expande a lista de x para ter mais pontos entre os valores originais
    x_range = expandir_lista(x, num_pontos)
    
    # Calcula os valores do polinômio nos pontos expandidos
    y_range = [sum(coef * (xi ** i) for i, coef in enumerate(coeficientes)) for xi in x_range]
    
    # Cria o gráfico
    plt.figure(figsize=(8, 6))  # Define o tamanho da figura
    plt.plot(x_range, y_range, color='darkblue', label="Polinômio Interpolador")  # Plota o polinômio interpolador
    plt.scatter(x, fx, color='red', marker='o', label="Pontos Originais (f(x))")  # Plota os pontos originais
    plt.xlabel("x")  # Rótulo do eixo x
    plt.ylabel("f(x)")  # Rótulo do eixo y
    plt.title("Interpolação Polinomial")  # Título do gráfico
    plt.legend()  # Exibe a legenda
    plt.grid(True)  # Exibe a grade no gráfico
    plt.show()  # Mostra o gráfico

# Exemplo de Testes
x_teste = [-1, 0, 1, 2]  # Exemplos de valores de x
fx_teste = [4, 1, -1, 7]  # Exemplos de valores correspondentes de f(x)

# Resolve o sistema para os valores de teste
resultado_teste = resolver_sistema(x_teste, fx_teste, exibir_detalhes=True)

# Plota o polinômio interpolador com os pontos originais
plotar_polinomio(x_teste, fx_teste, resultado_teste["Coeficientes"])

# Exibe o resultado da solução (matriz A, vetor b, coeficientes e se a solução é válida)
print(resultado_teste)







# Explicação Detalhada:
# 1. Função sistema_vandermonde(x, y):
# O que faz: Constrói a matriz de Vandermonde, que é usada para resolver sistemas lineares durante a interpolação polinomial. A matriz de Vandermonde tem a forma 
# 𝐴
# 𝑖
# 𝑗
# =
# 𝑥
# 𝑖
# 𝑗
# −
# 1
# A 
# ij
# ​
#  =x 
# i
# j−1
# ​
#  .
# Como usar: Você passa as listas de pontos 
# 𝑥
# x e 
# 𝑦
# y. A função retorna a matriz de Vandermonde 
# 𝐴
# A e o vetor 
# 𝑏
# b com os valores de 
# 𝑦
# y.
# 2. Função verificar_solucao(x, fx, coeficientes, exibir_detalhes=False):
# O que faz: Verifica se os coeficientes encontrados para o polinômio satisfazem as equações do sistema original.
# Como usar: Passa as listas de 
# 𝑥
# x e 
# 𝑓
# (
# 𝑥
# )
# f(x), além dos coeficientes. Pode ativar ou desativar a exibição de detalhes (erro, polinômio etc.).
# 3. Função resolver_sistema(x, fx, exibir_detalhes=False):
# O que faz: Resolve o sistema linear usando a matriz de Vandermonde e retorna os coeficientes do polinômio interpolador.
# Como usar: Passa os valores 
# 𝑥
# x e 
# 𝑓
# (
# 𝑥
# )
# f(x) e obtém os coeficientes do polinômio. Se quiser ver detalhes adicionais sobre a solução, pode ativar o parâmetro exibir_detalhes=True.
# 4. Função expandir_lista(lista, num_novos):
# O que faz: Expande uma lista de valores inserindo valores igualmente espaçados entre os valores originais.
# Como usar: Caso queira um gráfico mais suave, pode expandir os valores de 
# 𝑥
# x com mais pontos, usando expandir_lista.
# 5. Função plotar_polinomio(x, fx, coeficientes, num_pontos=100):
# O que faz: Plota o gráfico do polinômio interpolador junto com os pontos dados.
# Como usar: Fornece os pontos 
# 𝑥
# x e 
# 𝑓
# (
# 𝑥
# )
# f(x), os coeficientes do polinômio e o número de pontos a mais para o gráfico (quanto maior o número, mais suave o gráfico).
# 6. Testes:
# São realizados testes para verificar se as funções estão funcionando corretamente, com a impressão do resultado dos coeficientes e do gráfico gerado.
