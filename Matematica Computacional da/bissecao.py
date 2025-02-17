def bissecçao_metodo(func, a, b, tol=1e-6, max_iter=100):
    """
    Método de Bisseção para encontrar raízes de uma função.

    Parameters:
    func (function): Função para a qual a raiz será encontrada.
    a (float): Limite inferior do intervalo.
    b (float): Limite superior do intervalo.
    tol (float): Tolerância para o critério de parada.
    max_iter (int): Número máximo de iterações.

    Returns:
    float: Aproximação da raiz encontrada ou None se não convergir.
    """
    if func(a) * func(b) >= 0:
        print("Erro: A função deve ter sinais opostos em a e b.")
        return None

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2  # Ponto médio
        fc = func(c)

        if fc == 0:  # Encontrou a raiz exata
            return c

        # Verifica em qual subintervalo a raiz está
        if func(a) * fc < 0:
            b = c
        else:
            a = c

        iter_count += 1
        print(iter_count)

    # Retorna a aproximação da raiz
    return (a + b) / 2

# Exemplo de uso
def example_function(x):
    return x**3 - x - 2  # Função x³ - x - 2

# Intervalo inicial
a = 1
b = 2

# Chamando o método da posição falsa
root = bissecçao_metodo(example_function, a, b)

if root is not None:
    print(f"A raiz aproximada é: {root}")
else:
    print("A raiz não foi encontrada dentro do número máximo de iterações.")


