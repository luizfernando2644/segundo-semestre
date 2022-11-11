"""
- Implemente:
1- Crie um novo projeto e a classe Aluno.
2- Crie o construtor da classe com os atributos: nome, mensalidade, idade
3- No main, crie (instancie) pelo menos dois objetos da classe Aluno, teste
4- Crie os métodos gets (consulta) e sets (altera)
5- Use (teste) os métodos gets para os objetos criados
6- Use (teste) os métodos sets para os objetos criados
7- Crie o método retorna_dados, retorna todos os dados (atributos) concatenados. Teste
8- Crie o método mostra_dados. Não recebe e não retorna nada. Mostra os atributos. Teste
9- Crie o método aumento_mensalidade_valor, ele recebe o objeto e o valor do aumento. Teste
10- Crie o método aumento_mensalidade_porcentagem (recebe: 10%, 15% etc.). Teste
11- Crie o método que verifica se o aluno pode tirar a CNH e mostre mensagem apropriada.
12- Altere o construtor com estes valor default (padrão): mensalidade = 1000.0, idade = 18.
"""

class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_mensalidade(self):
        return self.mensalidade
    def set_mensalidade(self, valor):
        self.mensalidade = valor
    def get_idade(self):
        return self.idade
    def set_idade(self, nova_idade):
        self.idade = nova_idade
    def retorna_dados(self):
        dados = (f'{self.get_nome()}, {self.get_mensalidade()}, {self.get_idade()}')
        return dados

if __name__ == '__main__':
    aluno1 = Aluno('Paulo', 1100.00, 21)
    print(aluno1)
    aluno2 = Aluno('Carla', 900.00, 20)
    print(aluno2)
    print("-Aluno 1:")
    print("Nome:", aluno1.get_nome())
    print("Mensalidade:", aluno1.get_mensalidade())
    print("Idade:",aluno1.get_idade())
    print("-Aluno 2:")
    print("Nome:", aluno2.get_nome())
    print("Mensalidade:", aluno2.get_mensalidade())
    print("Idade:",aluno2.get_idade())
    nome1 = input("Novo nome: ")
    aluno1.set_nome(nome1)
    print("Nome atualizado:",aluno1.get_nome())
    aluno2.set_nome("Alice")
    print("Nome atualizado:",aluno2.get_nome())
    aluno1.set_mensalidade(1200.00)
    print("Nova mensalidade:",aluno1.get_mensalidade())
    print("Dados do aluno1:",aluno1.retorna_dados())
