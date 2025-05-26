class Carros:
    
    def __init__(self,nome,  marca, ano, cor):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.cor = cor
    
    def mostrar_infomaçoes(self):
        print (f" O {self.nome} é da marca {self.marca}, quem foi fabricado em {self.ano} da cor {self.cor}")
        
pessoa1 =  Carros(input("Qual é o nome do seu carro ? "), input("Qual a marca do seu carro? "), input("Qual o ano do seu carro ? "), input("Qual é a cor do seu carro? "))


pessoa1.mostrar_infomaçoes()