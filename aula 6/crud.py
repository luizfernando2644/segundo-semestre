lista = []
def menu():
    print("[c] - Create (inserir um item)")
    print("[r] - Read (mostrar toda a lista)")
    print("[u] - Update (substituir um item)")
    print("[d] - Delete  (remover um item)")
    print("[e] - Exit (sair)")
    o = input("Opcão: ")
    return o

def create():
    n = input("Insira um item:")
    lista.append(n)

def read():
    print(lista)

def update():
    i = (input("Digite o dado a ser inserido: "))
    ind = int(input("Digite a posição do elemento substituído: "))
    lista[ind] = i
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