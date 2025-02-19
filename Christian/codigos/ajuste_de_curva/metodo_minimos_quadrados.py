import numpy as np
import matplotlib.pyplot as plt
from numbers import Number

def construir_matriz_vandermonde(x, funcoes):
    """
    Constrói a matriz de projeto (Vandermonde) para o ajuste de mínimos quadrados.
    
    Parâmetros:
    x (numpy.ndarray): Vetor de entrada com os pontos x observados (1D, shape (n,))
    funcoes (list): Lista de funções base para criar a matriz. Cada função deve aceitar um escalar e retornar um escalar.
    
    Retorna:
    numpy.ndarray: Matriz de Vandermonde (shape (n, m)) onde n é o número de pontos e m o número de funções base
    
    Raises:
    TypeError: Se x não for numpy array ou funcoes não for lista
    ValueError: Se x estiver vazio ou funcoes vazia
    """
    # Validação de entradas
    if not isinstance(x, np.ndarray) or not isinstance(funcoes, list):
        raise TypeError("x deve ser numpy.ndarray e funcoes deve ser lista")
    if len(x) == 0 or len(funcoes) == 0:
        raise ValueError("x e funcoes não podem estar vazios")
    
    n = len(x)
    m = len(funcoes)
    X = np.zeros((n, m))
    
    # Preenche cada coluna da matriz com a aplicação das funções base nos pontos x
    for i in range(n):
        for j, f in enumerate(funcoes):
            try:
                X[i, j] = f(x[i])
            except Exception as e:
                raise ValueError(f"Função base {j} inválida para x={x[i]}: {e}")
    
    return X

def resolver_sistema_linear(A, b):
    """
    Resolve o sistema linear Ax = b usando eliminação de Gauss com pivotamento parcial.
    
    Parâmetros:
    A (numpy.ndarray): Matriz de coeficientes quadrada (shape (n,n))
    b (numpy.ndarray): Vetor de termos independentes (shape (n,))
    
    Retorna:
    numpy.ndarray: Vetor solução x (shape (n,))
    
    Raises:
    LinAlgError: Se a matriz for singular ou mal condicionada
    """
    # Validação de entradas
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A deve ser matriz quadrada")
    if A.shape[0] != b.shape[0]:
        raise ValueError("Dimensões de A e b incompatíveis")
    
    n = len(b)
    A = A.copy()
    b = b.copy()

    # Eliminação de Gauss com pivotamento parcial
    for i in range(n):
        # Encontra a linha com maior valor absoluto na coluna atual
        max_row = np.argmax(np.abs(A[i:, i])) + i
        
        # Verifica se a matriz é singular
        if np.isclose(A[max_row, i], 0):
            raise np.linalg.LinAlgError("Matriz singular - sistema sem solução única")
        
        # Troca linhas se necessário
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        
        # Eliminação para zerar elementos abaixo do pivô
        for j in range(i+1, n):
            fator = A[j, i] / A[i, i]
            A[j, i:] -= fator * A[i, i:]
            b[j] -= fator * b[i]

    # Substituição regressiva para encontrar a solução
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x

def minimos_quadrados(x, y, funcoes):
    """
    Ajusta um modelo linear usando mínimos quadrados ordinários (OLS).
    
    Parâmetros:
    x (numpy.ndarray): Variável independente (shape (n,))
    y (numpy.ndarray): Variável dependente (shape (n,))
    funcoes (list): Lista de funções base para o modelo
    
    Retorna:
    tuple: (coeficientes, funcao_ajustada) onde:
        - coeficientes (numpy.ndarray): Parâmetros otimizados do modelo
        - funcao_ajustada (callable): Função que aceita escalar e retorna predição
    
    Raises:
    ValueError: Se x e y tiverem tamanhos diferentes
    """
    # Validação de entradas
    if len(x) != len(y):
        raise ValueError("x e y devem ter o mesmo tamanho")
    
    # Construir matriz de projeto
    X = construir_matriz_vandermonde(x, funcoes)
    
    # Resolver sistema normal X^T X β = X^T y
    XT = X.T
    try:
        coeficientes = resolver_sistema_linear(XT @ X, XT @ y)
    except np.linalg.LinAlgError as e:
        raise ValueError("Problema mal condicionado. Tente reduzir o número de funções base") from e
    
    # Criar função ajustada
    def funcao_ajustada(novo_x):
        return sum(c * f(novo_x) for c, f in zip(coeficientes, funcoes))
    
    return coeficientes, funcao_ajustada

def plot_ajuste(x, y, funcao_final, is_non_linear=False):
    """
    Gera plot comparando dados observados com curva ajustada.
    
    Parâmetros:
    x (numpy.ndarray): Valores x observados
    y (numpy.ndarray): Valores y observados
    funcao_final (callable): Função ajustada para predizer novos valores y
    is_non_linear (bool): Indica se foi usada transformação não linear
    """
    # Criar grid suave para a curva ajustada
    x_min, x_max = np.min(x), np.max(x)
    x_plot = np.linspace(x_min - 0.5*(x_max-x_min), x_max + 0.5*(x_max-x_min), 200)
    
    # Calcular predições
    y_plot = funcao_final(x_plot)
    
    # Configurar plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='red', zorder=3, label='Dados Observados')
    plt.plot(x_plot, y_plot, 'b-', label='Modelo Ajustado')
    
    # Adicionar detalhes ao gráfico
    plt.title('Ajuste por Mínimos Quadrados\n', fontsize=14)
    plt.xlabel('Variável Independente (x)', fontsize=12)
    plt.ylabel('Variável Dependente (y)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Adicionar texto informativo
    plt.text(0.05, 0.95, 
             f'Tipo de Ajuste: {"Exponencial" if is_non_linear else "Polinomial"}',
             transform=plt.gca().transAxes,
             verticalalignment='top',
             bbox=dict(boxstyle='round', alpha=0.2))
    
    plt.show()

def validar_entrada(valor, tipo, tamanho=None):
    """Valida entradas e converte para numpy array se necessário"""
    if not isinstance(valor, np.ndarray):
        try:
            valor = np.asarray(valor, dtype=float)
        except:
            raise TypeError(f"Entrada deve ser conversível para numpy array, recebido {type(valor)}")
    
    if tamanho is not None and len(valor) != tamanho:
        raise ValueError(f"Tamanho incorreto. Esperado {tamanho}, recebido {len(valor)}")
    
    if np.any(np.isnan(valor)):
        raise ValueError("Entrada contém valores NaN")
    
    return valor

# Interface principal do programa
if __name__ == "__main__":
    try:
        # 🔄 Dados de Entrada (Exemplo)
        x_obs = validar_entrada([1, 2, 3, 4, 5], 'x')
        y_obs = validar_entrada([2.718, 1.484, 0.738, 0.367, 0.135], 'y', len(x_obs))
        
        # 🔄 Análise Inicial dos Dados
        print("🔍 Análise Exploratória Inicial:")
        print(f"Número de observações: {len(x_obs)}")
        print(f"Faixa de x: [{np.min(x_obs)}, {np.max(x_obs)}]")
        print(f"Média de y: {np.mean(y_obs):.3f} ± {np.std(y_obs):.3f}")

        # 🔄 Determinar Tipo de Ajuste
        is_non_linear = True  # Determina se usará transformação exponencial
        
        if is_non_linear:
            # Verificar viabilidade da transformação
            if np.any(y_obs <= 0):
                raise ValueError("Dados não-positivos impossibilitam transformação logarítmica")
            
            print("\n🔍 Transformação Não-Linear Aplicada:")
            print("Modelo original: y = exp(a + bx)")
            print("Transformação: ln(y) = a + bx")
            y_transformado = np.log(y_obs)
        else:
            y_transformado = y_obs.copy()

        # 🔄 Seleção de Funções Base
        if is_non_linear:
            funcoes = [lambda x: 1, lambda x: x]  # Modelo linear na escala log
        else:
            funcoes = [lambda x: 1, lambda x: x, lambda x: x**2]  # Modelo quadrático

        print("\n🔍 Funções Base Selecionadas:")
        for i, f in enumerate(funcoes):
            print(f"Função {i+1}: {f.__name__}")

        # 🔄 Ajuste do Modelo
        print("\n⚙️ Executando Ajuste por Mínimos Quadrados...")
        coeficientes, modelo = minimos_quadrados(x_obs, y_transformado, funcoes)
        
        # 🔄 Pós-Processamento
        if is_non_linear:
            def modelo_final(x):
                return np.exp(modelo(x))  # Reverte transformação logarítmica
        else:
            modelo_final = modelo

        # 🔄 Análise dos Resultados
        print("\n📊 Resultados do Ajuste:")
        print("Coeficientes estimados:")
        for i, c in enumerate(coeficientes):
            print(f"β{i}: {c:.5f}")
        
        # 🔄 Validação do Modelo
        y_pred = modelo_final(x_obs)
        residuos = y_obs - y_pred
        rss = np.sum(residuos**2)
        print(f"\n📈 Métricas de Qualidade:")
        print(f"Soma dos Quadrados dos Resíduos (RSS): {rss:.4f}")
        print(f"Erro Médio Absoluto (MAE): {np.mean(np.abs(residuos)):.4f}")

        # 🔄 Predição de Novos Valores
        novos_x = np.array([6, 7, 8])
        print("\n🔮 Predições para Novos Valores:")
        for x in novos_x:
            print(f"x = {x}: y_previsto = {modelo_final(x):.4f}")

        # 🔄 Visualização Gráfica
        print("\n🖨️ Gerando visualização gráfica...")
        plot_ajuste(x_obs, y_obs, modelo_final, is_non_linear)

    except Exception as e:
        print(f"\n❌ Erro na execução: {str(e)}")
        print("Verifique os dados de entrada e parâmetros de configuração")






#Fluxo do Programa:
#Entrada de Dados: Valida e converte os dados de entrada

#Análise Exploratória: Calcula estatísticas básicas

#Seleção de Modelo: Escolhe entre linear e não-linear

#Transformação de Dados: Aplica log se necessário

#Ajuste do Modelo: Calcula coeficientes via mínimos quadrados

#Pós-Processamento: Reverte transformações se aplicável

#Avaliação: Calcula métricas de qualidade

#Predição: Gera previsões para novos valores

#Visualização: Cria gráfico comparativo
