def metodo_ponto_fixo(g, x0, tol=1e-6, max_iter=100):
    """
    Refina a solução de uma equação usando o Método do Ponto Fixo para encontrar as raízes de f(x).

    Parâmetros:
        g (function): Função g(x) que define a transformação x = g(x).
        x0 (float): Chute inicial para o método.
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
        x_next = g(x_current)
        
        # Critério de parada: diferença entre iterações
        if abs(x_next - x_current) < tol:
            return x_next, i

        x_current = x_next

    raise ValueError("O método não convergiu dentro do número máximo de iterações.")

# Exemplo de uso para encontrar a raiz de f(x) = x^2 - 4
def g(x):
    return 0.5 * (x + 5 / x)  # g(x) é derivada de f(x) = x^2 - 4

def f(x):
    return x**2 - 5

x0 = 1.0  # Chute inicial
tol = 1e-6

try:
    raiz, iteracoes = metodo_ponto_fixo(g, x0, tol)
    print(f"A raiz encontrada é x = {raiz} após {iteracoes} iterações.")
    print(f"Verificação: f({raiz}) = {f(raiz)}")
except ValueError as e:
    print(e)
