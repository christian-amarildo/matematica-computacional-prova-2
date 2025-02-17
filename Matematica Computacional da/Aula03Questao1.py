S=0
sum = 0
for i in range (1,100001):
    sum+=0.1

S = 10000 - sum
print(f"Erro Absoluto para 𝑛 = 100000 e 𝑥 = 0.1: {abs(0 -S)}")
print(f"Erro Relativo para 𝑛 = 100000 e 𝑥 = 0.1: Não é possivel pois implica em divisão por zero")

S=0
sum = 0
for i in range (1,80001):
    sum+=0.125

S = 10000 - sum

print(f"Erro Absoluto para 𝑛 = 80000 e 𝑥 = 0.125: {abs(0 -S)}")
print(f"Erro Absoluto para 𝑛 = 80000 e 𝑥 = 0.125:  Não é possivel pois implica em divisão por zero")