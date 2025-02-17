def false_position_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Método da Posição Falsa para encontrar raízes de uma função.

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
    c = a  # Inicializa a variável para o cálculo da raiz

    while iter_count < max_iter:
        # Calcula o ponto de interseção linear (posição falsa)
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        fc = func(c)

        if abs(fc) < tol:  # Critério de parada: raiz encontrada
            return c

        # Atualiza os limites do intervalo com base no sinal de fc
        if func(a) * fc < 0:
            b = c
        else:
            a = c

        iter_count += 1
        print(iter_count)

    print("Aviso: Número máximo de iterações atingido.")
    return c  # Retorna a melhor aproximação encontrada

# Exemplo de uso
def example_function(x):
    return x**3 - x - 2  # Função x³ - x - 2

# Intervalo inicial
a = 1
b = 2

# Chamando o método da posição falsa
root = false_position_method(example_function, a, b)

if root is not None:
    print(f"A raiz aproximada é: {root}")
else:
    print("A raiz não foi encontrada dentro do número máximo de iterações.")
