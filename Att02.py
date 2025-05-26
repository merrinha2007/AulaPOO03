nome = input("Qual o seu nome? ").strip()

while True:
    if nome.isalpha():
        print(f"Ótimo, {nome}!")
        break
    else:
        print("Por favor, digite um nome válido (sem números).")

class Camisa:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def mostrar_camisa(self):
        return f"Camisa modelo {self.modelo}, marca {self.marca}"

class Tenis:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def mostrar_tenis(self):
        return f"Tênis modelo {self.modelo}, marca {self.marca}"

class Calca:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca

    def mostrar_calca(self):
        return f"Calça modelo {self.modelo}, marca {self.marca}"

# Coletar dados
pessoa_camisa = Camisa(input("Qual é o modelo da sua camisa? "), input("Qual é a marca da sua camisa? "))
pessoa_tenis = Tenis(input("Qual é o modelo do seu tênis? "), input("Qual é a marca do seu tênis? "))
pessoa_calca = Calca(input("Qual é o modelo da sua calça? "), input("Qual é a marca da sua calça? "))

class Pessoa:
    def __init__(self, nome, camisa, tenis, calca):
        self.nome = nome
        self.camisa = camisa
        self.tenis = tenis
        self.calca = calca

    def mostrar_pessoa(self):
        print(f"{self.nome} está vestindo:")
        print(self.camisa.mostrar_camisa())
        print(self.calca.mostrar_calca())
        print(self.tenis.mostrar_tenis())

# Criar objeto Pessoa e mostrar resultado
pessoa = Pessoa(nome, pessoa_camisa, pessoa_tenis, pessoa_calca)
pessoa.mostrar_pessoa()
