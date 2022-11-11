maior_nota = -1
ct = 0
maior_nota = float('-inf')
ct_maior = 0
print("Digite [-1] para sair")
while True:
    nota = float(input("Nota: "))
    if nota == -1:
        break
    if nota > maior_nota:
        maior_nota = nota
    elif nota == maior_nota:
        ct_maior += 1
print("Maior nota: ", maior_nota)
print("Qtd de alunos: ", ct)