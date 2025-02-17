def _metodo_newton_raphson(f, f_prime, x0, tol=1e-12, max_iter=1000):
    """
    Método de Newton-Raphson para encontrar as raízes de uma função.

    Parâmetros:
        f (function): Função para a qual queremos encontrar a raiz (f(x) = 0).
        f_prime (function): Derivada da função f(x).
        x0 (float): Chute inicial.
        tol (float): Tolerância para o critério de parada (default: 1e-6).
        max_iter (int): Número máximo de iterações (default: 100).

    Retorna:
        float: Aproximação para a raiz.
        int: Número de iterações realizadas.

    Lança:
        ValueError: Se o método não convergir dentro do número máximo de iterações.
    """
    x_current = x0

    for i in range(1, max_iter + 1):
        f_value = f(x_current)
        f_prime_value = f_prime(x_current)

        if f_prime_value == 0:
            raise ValueError("Derivada zero encontrada. O método falhou.")

        # Atualização de Newton-Raphson
        x_next = x_current - f_value / f_prime_value

        # Critério de parada
        if abs(x_next - x_current) < tol:
            return x_next, i

        x_current = x_next

    raise ValueError("O método não convergiu dentro do número máximo de iterações.")

# Exemplo de uso para encontrar a raiz de f(x) = x^2 - 4
def f(x):
    return x**2 - 8

def f_prime(x):
    return 2 * x

x0 = 1.0  # Chute inicial
tol = 1e-6

try:
    raiz, iteracoes = _metodo_newton_raphsonn(f, f_prime, x0, tol)
    print(f"A raiz encontrada é x = {raiz} após {iteracoes} iterações.")
    print(f"Verificação: f({raiz}) = {f(raiz)}")
except ValueError as e:
    print(e)
