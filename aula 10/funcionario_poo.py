"""- Implemente estes itens:
1- Crie a classe Funcionario com os atributos cpf, nome e salario
2- Crie o construtor da classe Funcionario def __init___ (self, ...)
3- Crie uma instância (objeto) da classe com os dados necessários (f1 = Funcionario()), teste
4- Crie alguns métodos get e set. Teste
4b-Crie um segundo funcionário passando apenas o cpf e o nome. Teste
5- Sobrescreva o método __str__. Ele recebe o objeto e retorna os dados do funcionário. Teste.
6- Crie a classe Gerente e o construtor com os atributos cpf, nome, salario, senha e a
   quantidade de funcionários que ele gerencia.
6b-Crie uma instância (objeto) da classe Gerente com os dados necessários, teste
7- Crie alguns métodos gets e sets. Teste
8- Mostre todos os dados (atributos) do objeto g1 da classe Gerente, conseguiu usando o __str__?
9- Crie o método autentica na classe Gerente. Ele recebe o objeto, o usuário digita a senha
   e verifica se a senha digitada é igual a senha armazenada na memória (self.senha).
   imprime: "Acesso permitido." ou "Acesso negado." e retorna o valor booleano True ou False.
10- Use o método autentica para o gerente instanciado (objeto g1).
11- Use o método autentica para o funcionario instanciado (objeto f1). Por quê deu erro?
12- Crie outra instância (objeto g2) da classe Gerente com os dados necessários.
13- Use o método __str__ para o gerente (objeto g2). Por quê mostrou endereço hexadecimal?
14- Use todos os métodos da classe Gerente para o gerente g2."""

     

class Funcionario:
    def __init__(self, cpf, nome, salario=0.0):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        self.salario = novo_salario

    def __str__(self):
        i = f"Nome: {self.nome}, CPF: {self.cpf}, salário: {self.salario:.2f}"
        return i

class Gerente(Funcionario):  #class Subclasse(Superclasse)
    def __init__(self, cpf, nome, salario, senha, qtd_func=0): #vai herdar características da superclasse
        super().__init__(cpf, nome, salario)
        self.senha = senha
        self.qtd_func = qtd_func

    def get_nome(self):
        return self.nome
    '''def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_cpf(self):
        return self.cpf
    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf

    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        self.salario = novo_salario'''

    def get_senha(self):
        return self.senha
    def set_senha(self, nova_senha):
        self.senha = nova_senha

    def get_qtd_func(self):
        return self.qtd_func
    def set_senha(self, novos_func):
        self.novos_func = novos_func

    def __str__(self):
        i = f"Nome: {self.nome}, CPF: {self.cpf}, salário: {self.salario:.2f}, senha: {self.senha}, quantidade de funcionarios: {self.qtd_func}"
        return i

    def autentica(self):
        senha = input("Senha: ")
        if senha == self.senha:
            print("Acesso permitido.")
            return True
        else:
            print("Acesso negado.")
            return False

    


if __name__ == '__main__':
    gerente = Gerente(999, 'Adalberto', 500.00, 'masco123', 100)
    funcionario1 = Funcionario(123, 'Cleber', 200.00)
    funcionario2 = Funcionario(456, 'Jorge')
    print(gerente)
    print(funcionario1)
    novo_nome = input("Digite um novo nome para o funcionário 1: ")
    funcionario1.set_nome(novo_nome)
    print("------------------------------------------------")
    novo_cpf = input("CPF do novo funcionario: ")
    funcionario1.set_cpf(novo_cpf)
    print("Novo nome: ",funcionario1.get_nome())
    print("Novo CPF: ",funcionario1.get_cpf())  
    gerente.autentica()