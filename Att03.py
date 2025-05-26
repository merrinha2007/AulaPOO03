class ContaBancaria: # Eu pedi ajuda ao ChatGpt, Estava confuso com alguns parametros, mas a escrita e minha e a logica tambem, mas teve algumas correções para simplificar
    
    def __init__(self, saldo):
        self.saldo = float(saldo)
    
    def mostrar_saldo(self):
        print(f"O seu saldo é de R$ {self.saldo}")
    
    def depositar(self, valor):
        valor = float(valor)
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado com sucesso.")
        self.mostrar_saldo()
    
    def retirar(self, valor):
        valor = float(valor)
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Retirada de R$ {valor} realizada com sucesso.")
        else:
            print("Saldo insuficiente para a retirada.")
        self.mostrar_saldo()

#Execução principal 

saldo_inicial = input("Qual o saldo da sua conta? ")
conta = ContaBancaria(saldo_inicial)

escolha = input("Deseja fazer uma retirada ou depósito? ").strip()

if escolha == 'retirada':
    valor_retirada = input("Qual o valor da sua retirada? ")
    conta.retirar(valor_retirada)

elif escolha == 'depósito' or escolha == 'deposito':
    valor_deposito = input("Qual o valor do seu depósito? ")
    conta.depositar(valor_deposito)

else:
    print("Opção inválida.")
