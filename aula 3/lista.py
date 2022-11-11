l_cnpj = []
l_qtd = []
print("Digite <enter> para sair.")
while True:
    cnpj = int(input("Digite o CNPJ: "))
    if cnpj == '':
        break
    l_cnpj.append(cnpj)
    qtd = int(input("Quantidade de funcionários: "))
    l_qtd.append(qtd)
maior_qtd = max(l_qtd)
indice = l_qtd.index(maior_qtd)
maior_cnpj = l_cnpj[indice]
print(f"Empresa {maior_cnpj} tem maior numero de funcionarios com {maior_qtd}.")
print(f"Empresa" + maior_cnpj + "tem maior numero de funcionarios", maior_qtd)