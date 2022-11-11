
"""- Implemente:
1- Crie um projeto e a classe Veiculo
2- Crie o construtor da classe com os atributos: modelo, ano, valor
3- No main, crie pelo menos dois objetos da classe. Teste
4- Crie os métodos gets e sets dos atributos. Teste os gets
   def get_nome_atributo1(self):                   # Modelo do método get (consulta)
       return self.nome_atributo1
   def set_nome_atributo1(self, valor):            # Modelo do método set (altera)
       self.nome_atributo1 = valor
5- Com o método set_modelo, altere o modelo do veiculo. Teste
6- Altere o valor do veiculo, com o método set_valor. Teste
7- Faça uma crítica no método set_valor para evitar dados inconsistentes. Teste
8- Crie o método mostra_dados. Ele mostra todos os atributos da classe. Teste
9- Crie o método retorna_dados, ele retorna os dados (atritutos) concatenados. Teste
10- Crie o método aumento_valor. Ele recebe o valor do aumento em reais que será
    acrescentado ao atributo valor do carro. Teste
11- Peça pro usuário fornecer o valor do aumento do veículo. Teste
12- Altere o construtor para o usuário instanciar um objeto sem valor, valor default 0.
    Ele fornece somente o modelo e ano. Teste, crie um novo objeto só com o modelo e ano.
13- Crie mais um objeto passando apenas o modelo do veículo, teste
14- Crie mais um objeto passando apenas o modelo e o valor, não passe o argumento ano
    , teste"""



class Veiculo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def get_modelo(self):
        return self.modelo
    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo
    
    def get_ano(self):
        return self.ano
    def set_ano(self, novo_ano):
        self.ano = novo_ano

    def get_valor(self):
        return self.valor
        
    def set_valor(self, nv):
        if nv > 0:
            self.valor = nv
        else:
            print("---------------")
            print("Valor inválido")


    def retorna_dados(self):
        dados = (f"{self.get_modelo()}, {self.get_ano()}, {self.get_valor()}")
        return dados

    def aumento_valor(self):
        soma = int(input("Digite o valor a acrescentar: "))
        self.valor = self.valor + soma
    



if __name__ == '__main__':
    veiculo1 = Veiculo('Gol bolinha', 2000, 20)
    veiculo2 = Veiculo('Camaro amarelo', 2012, 100)
    print(veiculo1)
    print("Modelo:",veiculo1.get_modelo())
    print("Ano:",veiculo1.get_ano())
    print("Valor:",veiculo1.get_valor())

    print(veiculo2)
    print("Modelo: ",veiculo2.get_modelo())
    print("Ano:",veiculo2.get_ano())
    print("Valor:", veiculo2.get_valor())

    novo_modelo1 = input("Novo modelo para o veículo 1: ")
    veiculo1.set_modelo(novo_modelo1)
    novo_ano1 = int(input("Novo ano para o veículo 1: "))
    veiculo1.set_ano(novo_ano1)
    nv = int(input("Novo valor: "))
    veiculo1.set_valor(nv)
    print("----------------")
    print("Modelo atualizado do veículo 1: ",veiculo1.get_modelo())
    print("Ano atualizado do veículo 1: ",veiculo1.get_ano())
    print("Valor atualizado do veículo 1: ",veiculo1.get_valor())
    print("----------------")
    
    

    novo_modelo2 = input("Novo modelo para o veículo 2: ")
    veiculo2.set_modelo(novo_modelo2)
    novo_ano2 = int(input("Novo ano para o veículo 2: "))
    veiculo2.set_ano(novo_ano2)
    nv = int(input("Novo valor: "))
    veiculo2.set_valor(nv)
    print("----------------")
    print("Modelo atualizado do veículo 2: ",veiculo2.get_modelo())
    print("Ano atualizado do veículo 2: ",veiculo1.get_ano())
    print("Valor atualizado do veículo 2: ",veiculo2.get_valor())
    print("----------------")

    print("Dados do veículo 1: \n",veiculo1.retorna_dados())
    print("-----------------------------------------------")
    print("Dados do veículo 2: \n",veiculo2.retorna_dados())
    
    print("----------------")
    print("Aumento do preço")
    veiculo1.aumento_valor()
    print("Novo valor do veículo 1:",veiculo1.get_valor())
    print("----------------")
    veiculo2.aumento_valor()
    print("Novo valor do veículo 2:", veiculo1.aumento_valor())

    
