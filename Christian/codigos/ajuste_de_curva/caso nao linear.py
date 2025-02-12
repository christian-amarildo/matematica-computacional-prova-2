import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def ajuste_nao_linear(x, y, modelo, palpite_inicial=None, max_iter=1000):
    """
    Realiza ajuste não linear pelo método dos mínimos quadrados
    
    Parâmetros:
    x (array): Dados de entrada
    y (array): Dados de saída
    modelo (função): Função modelo para ajuste f(x, *params)
    palpite_inicial (list): Valores iniciais para os parâmetros
    max_iter (int): Número máximo de iterações
    
    Retorna:
    parametros_otimos (array): Parâmetros otimizados
    covariancia (matrix): Matriz de covariância
    mse (float): Erro quadrático médio
    """
    
    try:
        # Conversão e validação dos dados
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)
        
        if x.shape != y.shape:
            raise ValueError("x e y devem ter o mesmo tamanho")
            
        if len(x) < len(palpite_inicial):
            raise ValueError(f"Necessário mínimo de {len(palpite_inicial)} pontos")
            
    except Exception as e:
        print("\nERRO NA VALIDAÇÃO DOS DADOS:")
        print(f"Tipo: {type(e).__name__}")
        print(f"Detalhes: {str(e)}")
        print("Soluções possíveis:")
        print("- Verificar consistência entre x e y")
        print("- Garantir que todos valores são numéricos")
        print("- Usar mais pontos que parâmetros no modelo")
        raise
    
    tentativas = [
        {'method': 'lm', 'maxfev': max_iter},  # Levenberg-Marquardt
        {'method': 'trf', 'max_nfev': max_iter}, # Trust Region Reflective
        {'method': 'dogbox', 'max_nfev': max_iter}
    ]
    
    for i, config in enumerate(tentativas):
        try:
            print(f"\nTentativa {i+1} com método {config['method']}")
            
            parametros_otimos, covariancia = curve_fit(
                f = modelo,
                xdata = x,
                ydata = y,
                p0 = palpite_inicial,
                **config
            )
            
            # Verificação de convergência
            if np.isinf(covariancia).any():
                raise RuntimeError("Matriz de covariância contém infinitos")
                
            break
                
        except Exception as e:
            print(f"\nFalha na tentativa {i+1}:")
            print(f"Erro: {type(e).__name__}")
            print(f"Detalhes: {str(e)}")
            
            if i == len(tentativas)-1:
                print("\nTODAS AS TENTATIVAS FALHARAM!")
                print("Possíveis causas:")
                print("1. Palpite inicial inadequado")
                print("2. Modelo mal especificado")
                print("3. Dados insuficientes ou ruidosos")
                print("4. Não convergência numérica")
                print("Soluções sugeridas:")
                print("- Melhorar palpite inicial")
                print("- Simplificar o modelo")
                print("- Aumentar max_iter")
                print("- Pré-processar os dados")
                raise
                
            # Ajuste para próxima tentativa
            if palpite_inicial:
                palpite_inicial = [p*(1 + 0.1*np.random.randn()) for p in palpite_inicial]
    
    # Cálculo de métricas
    residuos = y - modelo(x, *parametros_otimos)
    mse = np.mean(residuos**2)
    ss_res = np.sum(residuos**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r2 = 1 - (ss_res / ss_tot)
    
    # Plotagem
    plt.figure(figsize=(10,6))
    plt.scatter(x, y, label='Dados Originais', color='red')
    
    x_ajuste = np.linspace(min(x), max(x), 500)
    y_ajuste = modelo(x_ajuste, *parametros_otimos)
    
    plt.plot(x_ajuste, y_ajuste, label='Curva Ajustada', color='blue')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Ajuste Não Linear por Mínimos Quadrados')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return parametros_otimos, covariancia, mse, r2

# Exemplo de uso:
if __name__ == "__main__":
    # Modelo 1: Exponencial decrescente y = a*exp(-b*x) + c
    def modelo_exp(x, a, b, c):
        return a * np.exp(-b * x) + c
    
    # Gerar dados sintéticos com ruído
    x_data = np.linspace(0, 5, 50)
    y_data = 2.5 * np.exp(-1.3 * x_data) + 0.5 + np.random.normal(0, 0.1, 50)
    
    try:
        print("Exemplo de ajuste exponencial:")
        params, cov, mse, r2 = ajuste_nao_linear(
            x = x_data,
            y = y_data,
            modelo = modelo_exp,
            palpite_inicial = [1, 0.5, 0], # Palpite inicial crítico!
            max_iter = 2000
        )
        
        print("\nResultado do ajuste:")
        print(f"Parâmetros otimizados: a={params[0]:.3f}, b={params[1]:.3f}, c={params[2]:.3f}")
        print(f"MSE: {mse:.4f}")
        print(f"R²: {r2:.4f}")
        
    except Exception as e:
        print("\nFalha no exemplo:")
        print(f"Erro final: {str(e)}")
