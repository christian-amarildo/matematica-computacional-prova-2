import numpy as np

def calcular_area_trapezio(x0: float, x1: float, num_intervalos: int, funcao) -> float:
    """
    Calcula a área sob a curva definida por `funcao` no intervalo [x0, x1]
    utilizando a regra do trapézio com `num_intervalos` subintervalos.
    
    Parâmetros:
        x0 (float): Limite inferior do intervalo.
        x1 (float): Limite superior do intervalo.
        num_intervalos (int): Número de subintervalos.
        funcao (callable): Função a ser integrada.
    
    Retorna:
        float: Aproximação da integral no intervalo dado.
    """
    # Calcula o tamanho do passo
    passo = (x1 - x0) / num_intervalos
    
    # Lista de valores da função nos pontos relevantes
    valores_y = [funcao(x0)] + [2 * funcao(x0 + i * passo) for i in range(1, num_intervalos)] + [funcao(x1)]
    
    # Aplicação da fórmula da regra do trapézio
    area_aproximada = (passo * 0.5) * sum(valores_y)
    return area_aproximada

def funcao_exemplo(x: float) -> float:
    """Exemplo de função para integração: f(x) = x² * ln(x) + 1"""
    return (x**2) * np.log(x) + 1

if __name__ == "__main__":
    # Exemplo de uso da função
    resultado = calcular_area_trapezio(1.2, 1.4, 2, funcao_exemplo)
    print(f"Área aproximada: {resultado:.6f}")
