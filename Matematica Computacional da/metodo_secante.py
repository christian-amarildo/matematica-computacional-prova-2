def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Método da Secante para encontrar as raízes de uma função.

    Parâmetros:
        f (function): Função para a qual queremos encontrar a raiz (f(x) = 0).
        x0 (float): Primeiro chute inicial.
        x1 (float): Segundo chute inicial.
        tol (float): Tolerância para o critério de parada (default: 1e-6).
        max_iter (int): Número máximo de iterações (default: 100).

    Retorna:
        float: Aproximação para a raiz.
        int: Número de iterações realizadas.

    Lança:
        ValueError: Se o método não convergir dentro do número máximo de iterações.
    """
    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            raise ValueError("Denominador zero encontrado. O método falhou.")

        # Fórmula da secante
        x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        # Critério de parada
        if abs(x_next - x1) < tol:
            return x_next, i

        x0, x1 = x1, x_next

    raise ValueError("O método não convergiu dentro do número máximo de iterações.")

# Exemplo de uso para encontrar a raiz de f(x) = x^2 - 4
def f(x):
    return x**3 - 4

x0 = 1.0  # Primeiro chute inicial
x1 = 2.0  # Segundo chute inicial
tol = 1e-6

try:
    raiz, iteracoes = secant_method(f, x0, x1, tol)
    print(f"A raiz encontrada é x = {raiz} após {iteracoes} iterações.")
    print(f"Verificação: f({raiz}) = {f(raiz)}")
except ValueError as e:
    print(e)
