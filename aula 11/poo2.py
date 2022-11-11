'''1- Crie a superclasse Veiculo e o construtor (__init__) com os atributos comuns valor,
   modelo (Corolla, Honda,Pálio etc) e km que indica a quilometragem do veículo.

2- Crie alguns métodos gets e sets.

3- Antes do método main, crie a subclasse Carro, que herda da superclasse Veiculo. E o
   construtor com os atributos valor, modelo, km e qtd_portas. E os métodos get e set.

4- Crie três instâncias da subclasse Carro com quatro, três e dois argumentos, teste

5- Na classe Carro, sobrescreva o método __str__ do Python, ele retorna todos os dados
   (atributos), teste

6- Antes do método main, crie a subclasse Moto, que herda a superclasse Veiculo. E o
   construtor com os três atributos comuns e o atributo cilindradas. E os métodos get e set

7- Crie duas instâncias (objetos) da classe Moto com quatro e três argumentos. Teste

8- Utilize o método vars() para acessar os atributos de Carro e Moto num dicionário.
   Ex.: print(vars(objeto))

9- Use o método __dict__ para acessar os atributos de Carro e Moto num dicionário.
   Ex.: print(objeto.__dict__)

10- Crie o método atualiza valor, ele recebe um valor em reais e não retorna nada. O método
    acrescenta o valor recebido ao valor de qualquer veículo. Teste.

10b- Refaça o item anterior com críticas (filtros) dentro da função.

11- Crie o método atualiza_valor_pct, ele recebe a porcentagem (5, 10, 20 etc) e não
    retorna nada. O método atualiza o valor de qualquer veículo. Faça crítica e teste.

12- Crie o método situacao do veículo para mostrar se é veículo zero, veículo seminovo
    ou veículo usado. O veiculo zero tem km igual a zero, seminovo se tiver até 20000 Km e
    veículo usado se tiver mais que 20000 Km. Use o método com os objetos criados.

13- Crie o método situacao_2 para substituir a mensagem 'Veículo zero' por uma mensagem
    mais específica 'Carro zero' ou 'Moto zero' e assim sucessivamente com as outras
    mensagens. Teste

14- O valor do IPVA de um carro é 3% do valor do carro mais uma taxa de R$ 100. E o valor
    do IPVA de uma moto é 2% do valor da moto. Onde vai ser criado o método cálculo do IPVA

15- Refaça o item anterior, crie um único método na superclasse (calculo_ipva_2)'''





'''Veículo -> valor, modelo, quilometragem
   Carro -> quantidade de portas
   Moto -> cilindradas'''


class Veiculo():
    def __init__(self, valor, modelo, km):
        self.valor = valor
        self.modelo = modelo
        self.km = km

    def get_valor(self):
        return self.valor
    def get_modelo(self):
        return self.modelo
    def get_km(self):
        return self.km

    def set_valor(self, nv):
        self.valor = nv
    def set_modelo(self, novo_m):
        self.modelo = novo_m
    def set_km(self, nova_km):
        self.km = nova_km

    def atualiza_valor(self, vlr_aumento):
        if vlr_aumento > 0:
            self.valor += vlr_aumento
        else:
            print("Erro")
    
    
    
    

class Carro(Veiculo):
    def __init__(self, valor, modelo, km=0, qtd_portas=4):
        super().__init__(valor, modelo, km)
        self.qtd_portas = qtd_portas

    def get_qtd_portas(self):
        return self.qtd_portas

    def set_qtd_portas(self, novas_p):
        self.qtd_portas = novas_p
    def __str__(self):
        i = f"Modelo: {self.modelo}\nValor: {self.valor:.2f}\nQuilometragem: {self.km}\nQuantidade de portas: {self.qtd_portas}"
        return i



class Moto(Veiculo):
    def __init__(self, valor, modelo, km, cilindradas=0):
        super().__init__(valor, modelo, km)
        self.cilindradas = cilindradas
    
    def get_cilindradas(self):
        return self.cilindradas

    def set_cilindradas(self, novas_c):
        self.cilindradas = novas_c
    def __str__(self):
        i = f"Modelo: {self.modelo}\nValor: {self.valor:.2f}\nQuilometragem: {self.km}\nCilindradas: {self.cilindradas}"
        return i
    

if __name__ == "__main__":
    veiculo1 = Carro(20000.00, 'Fiorino', 500, 4)
    print("------ Veículo 1 ------")
    print(veiculo1)
    (veiculo1.atualiza_valor(float(input("Aumento: "))))
    print(f"Valor atualizado: {veiculo1.get_valor()} reais")
    print("-----------------------")
    veiculo2 = Carro(50000.00, 'HB20', 0)
    print("------ Veículo 2 ------")
    print(veiculo2)
    print("-----------------------")
    veiculo3 = Carro(100000.00, 'Mercedes')
    print("------ Veículo 3 ------")
    print(veiculo3)
    print("-----------------------")
    veiculo4 = Moto(15000.00, 'Pop100', 200, 300)
    print("------ Veículo 4 ------")
    print(veiculo4)
    print("-----------------------")
    veiculo5 = Moto(20000.00, 'Suzuki', 150)
    print("------ Veículo 5 ------")
    print(veiculo5)
    print("-----------------------")