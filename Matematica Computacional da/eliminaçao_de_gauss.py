import numpy as np

def eliminacao_de_gauss(matriz):
    """
    Realiza a eliminação de Gauss para escalonar uma matriz.

    Parâmetros:
        matriz (list ou numpy.ndarray): Matriz de coeficientes aumentada.

    Retorna:
        numpy.ndarray: Matriz escalonada.
    """
    
    matriz = np.array(matriz, dtype=float)
    
    linhas, colunas = matriz.shape

    for i in range(min(linhas, colunas)):
        # Busca o maior pivô em módulo na coluna atual
        max_row = i + np.argmax(np.abs(matriz[i:, i]))
        
        # Troca a linha atual com a linha do maior pivô
        if matriz[max_row, i] != 0:
            matriz[[i, max_row]] = matriz[[max_row, i]]

            # Eliminação
            for j in range(i + 1, linhas):
                fator = matriz[j, i] / matriz[i, i]
                matriz[j, i:] -= fator * matriz[i, i:]

    return matriz

# Exemplo de uso
if __name__ == "__main__":
    # Matriz aumentada (exemplo)
    matriz = [
        [2, 1, -1, 8],
        [-3, -1, 2, -11],
        [-2, 1, 2, -3],
        [1, 2, 3, 4]
    ]

    matriz_escalonada = eliminacao_de_gauss(matriz)
    print("Matriz escalonada:")
    print(matriz_escalonada)
