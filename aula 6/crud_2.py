lista = []
l = ("c", "r", "u", "d", "e")
def menu():
    while True:
        print("[c] - Create (inserir um item)")
        print("[r] - Read (mostrar toda a lista)")
        print("[u] - Update (substituir um item)")
        print("[d] - Delete  (remover um item)")
        print("[e] - Exit (sair)")
        l = ["c", "r", "u", "d", "e"]
        o = input("Opcão: ").lower()
        if o not in l:
            print("Opção inválida\nDigite uma opçao válida")
            continue
        else:
            return o
        
def create():
    while True:
        n = input("Insira um item: ")
        if n == '':
            break
        lista.append(n)

def read():
    print(lista)
    if lista != []:
        for n in range(0, len(lista)):
            print(n, lista[n])


def update():
    if lista == []:
        print("A lista está vazia.")
    elif lista != []:
        try:
            i = (input("Digite o dado a ser inserido: "))
            ind = int(input("Digite a posição do elemento substituído: "))
            lista[ind] = i

        except IndexError:
            print("O valor citado não está na lista")

    print(lista)

def delete():
    r = (input("Digite o item a ser removido: "))
    lista.remove(r)
    print(lista)


if __name__ == '__main__':
    while True:
        op = menu()
        if op == "c":
            create()
        elif op == "r":
            read()
        elif op == "u":
            update()
        elif op == "d":
            delete()
        else:
            break