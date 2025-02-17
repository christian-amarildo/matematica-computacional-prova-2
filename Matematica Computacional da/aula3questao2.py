
def questao2():
    
  A = 1
  s = 2
  while s>1 :
        A = A/2
        s = 1 + A
  Prec = 2*A

  return Prec  

print(f"Valor de Precisão: {questao2()}")
print("A) Python possui apenas precisão dupla")
print("""B) Pois a ultima divisão por 2 de A é aquela que quebra a precisão, então é preciso dar um passo
atras para voltar ao valor correto""")


print("C)")

def algoritmo_customizado(valor_referencia):
    # Passo 1: Inicializando A e s
    A = 1.0  # Precisão dupla (padrão)
    s = valor_referencia + 1  # Referência mais 1

    # Passo 2: Laço até que s seja menor ou igual ao valor de referência
    while s > valor_referencia:
        A = A / 2
        s = valor_referencia + A

    # Passo 3: Calculando a precisão estimada
    Prec = 2 * A
    return Prec

# Testando para os valores fornecidos
valores_referencia = [10, 17, 100, 184, 1000, 1575, 10000, 17893]
resultados = []

for valor in valores_referencia:
    resultado = algoritmo_customizado(valor)
    resultados.append((valor, resultado))

# Exibindo os resultados
print("Resultados em precisão dupla:")
for ref, prec in resultados:
    print(f"Valor de referência: {ref}, Precisão estimada: {prec}")
    
print("O valor altera pois numeros maiores ocupam mais espaço de bits, então quando o valor de A é somado com a referencia, mais rapidamente o limite de bits é atingido")
