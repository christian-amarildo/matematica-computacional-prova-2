import numpy as np

def calcular_regra13simpson(x0: float, x1: float, num_intervalos: int, funcao) -> float:
    """
    Calcula a aproximação da integral definida usando a Regra 1/3 de Simpson.

    Parâmetros:
    x0 (float): Limite inferior da integral.
    x1 (float): Limite superior da integral.
    num_intervalos (int): Número de subintervalos (deve ser par).
    funcao (callable): Função a ser integrada.

    Retorna:
    float: Aproximação da integral ou None caso o número de subintervalos seja ímpar.
    """
    if num_intervalos % 2 != 0:
        print("Erro: O número de subintervalos deve ser par.")
        return None
    
    # Calcula o tamanho do passo
    h = (x1 - x0) / num_intervalos
    
    # Lista de valores da função nos pontos relevantes
    valores_y = [funcao(x0)]  # f(x0)
    
    # Aplicação dos coeficientes 4 e 2 para pontos internos
    for i in range(1, num_intervalos):
        x_i = x0 + (h * i)
        coeficiente = 4 if i % 2 == 1 else 2  # Ímpares recebem 4, pares recebem 2
        valores_y.append(coeficiente * funcao(x_i))
    
    # Adiciona f(x1)
    valores_y.append(funcao(x1))
    
    # Aplicação da fórmula da Regra de Simpson 1/3
    area_aproximada = (h / 3) * sum(valores_y)
    
    return area_aproximada

def funcao_exemplo(x: float) -> float:
    """
    Exemplo de função para integração: f(x) = sqrt(x) + 1/x
    """
    return np.sqrt(x) + 1/x

if __name__ == "__main__":
    # Exemplo de uso da função
    resultado = calcular_regra13simpson(1.4, 1.8, 4, funcao_exemplo)
    print(f"Área aproximada: {resultado:.6f}")
