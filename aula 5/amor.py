import math
numeros = []
print("Digite [0] para sair")
ct = 0
while True:
    n = float(input("Digite um valor: "))
    if n == 0:
        break
    numeros.append(n)
    sum(numeros)
print(numeros)
print(f"A quantidade de elementos da lista é {len(numeros)}.")
print(f"A soma dos números da lista é {sum(numeros)}.")
print(f"O maior valor da lista é {max(numeros)}.")
print(f"O menor valor da lista é {min(numeros)}.")
x = int(input("Digite um valor e veja se está na lista: "))
if x in numeros: 
    print(f"De fato, o valor {x} está na lista.")
    print(f"O índice dele é {numeros.index(x)}.")
else:
    print(f"O valor {x} não está na lista")
numeros.insert(1, 33)
numeros.sort()
print(f"A lista em ordem crescente é {numeros}")
numeros.sort(reverse = True)
print(f"A lista em ordem decrescente é {numeros}")
print(f"A média dos termos é {sum(numeros)/len(numeros):.3f}")

ct = 0
for numero in numeros:
    if numero > 10:
        ct = ct + 1
print(f"{ct/len(numeros)*100}%")