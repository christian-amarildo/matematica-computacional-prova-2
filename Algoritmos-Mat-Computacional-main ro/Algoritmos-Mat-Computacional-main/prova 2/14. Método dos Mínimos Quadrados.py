import numpy as np
import matplotlib.pyplot as plt

def minimos_quadrados(x_tab, y_tab, tipo_funcao='polinomial', grau=1, **params):
    """
    Realiza ajuste de curva pelo método dos mínimos quadrados
    Parâmetros:
        x_tab -- array com os pontos x de dados
        y_tab -- array com os valores correspondentes y
        tipo_funcao -- tipo de função para ajuste ('polinomial', 'exponencial', 'logaritmica')
        grau -- grau do polinômio (quando tipo_funcao='polinomial')
        params -- parâmetros adicionais específicos para cada tipo de função
    Retorna:
        coeficientes -- array com os coeficientes do ajuste
    """
    if tipo_funcao == 'polinomial':
        # Cria a matriz X para o sistema Ax = b
        X = np.ones((len(x_tab), grau + 1))
        for i in range(1, grau + 1):
            X[:, i] = x_tab ** i
        coeficientes = np.linalg.lstsq(X, y_tab, rcond=None)[0]
        
    elif tipo_funcao == 'exponencial':
        # Ajuste exponencial: y = a * exp(b*x)
        def func_exp(x, a, b):
            return a * np.exp(b * x)
        
        from scipy.optimize import curve_fit
        coeficientes, _ = curve_fit(func_exp, x_tab, y_tab, 
                                  p0=[1.0, 1.0])
        
    elif tipo_funcao == 'logaritmica':
        # Ajuste logarítmico: y = a * log(b*x + c)
        def func_log(x, a, b, c):
            return a * np.log(b * x + c)
        
        from scipy.optimize import curve_fit
        coeficientes, _ = curve_fit(func_log, x_tab, y_tab, 
                                  p0=[1.0, 1.0, 1.0])
        
    return coeficientes

def avalia_funcao(x, coeficientes, tipo_funcao):
    """
    Avalia a função ajustada em um ponto x
    Parâmetros:
        x -- ponto onde avaliar a função
        coeficientes -- array com os coeficientes do ajuste
        tipo_funcao -- tipo de função para ajuste
    Retorna:
        valor da função em x
    """
    if tipo_funcao == 'polinomial':
        resultado = 0
        for i, coef in enumerate(coeficientes):
            resultado += coef * (x ** i)
        return resultado
    
    elif tipo_funcao == 'exponencial':
        return coeficientes[0] * np.exp(coeficientes[1] * x)
    
    elif tipo_funcao == 'logaritmica':
        return coeficientes[0] * np.log(coeficientes[1] * x + coeficientes[2])

# Exemplo de uso
x_tab = np.array([1., 2., 3., 4.])
y_tab = np.array([2., 3., 5., 7.])

# Escolha o tipo de função e seus parâmetros
tipo_funcao = 'polinomial'  # 'polinomial', 'exponencial', 'logaritmica'
grau = 1  # apenas para polinomial

# Calcula os coeficientes
coeficientes = minimos_quadrados(x_tab, y_tab, tipo_funcao, grau)

# Cria pontos para plotagem suave
x_plot = np.linspace(min(x_tab)-0.5, max(x_tab)+0.5, 1000)
y_plot = [avalia_funcao(x, coeficientes, tipo_funcao) for x in x_plot]

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(x_plot, y_plot, 'b-', label=f'Ajuste {tipo_funcao}')
plt.scatter(x_tab, y_tab, color='red', marker='o', s=100, 
           label='Pontos originais')
plt.grid(True)
plt.legend()
plt.title(f'Ajuste de Curva pelo Método dos Mínimos Quadrados\n({tipo_funcao})')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

print(f"Coeficientes do ajuste {tipo_funcao}:")
print(coeficientes)