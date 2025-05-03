
# Código procedural - Sistema bancário
# saldo = 500 # atributo
# # Funções -> Métodos

# def depositar(s):
#     valor = float(input('Digite o valor a ser depositado: '))
#     s += valor
#     return s
#     # saldo = saldo + valor

# def sacar(saldo):
#     valor = float(input('Digite o valor a ser depositado: '))
#     if valor <= saldo:
#         saldo -= valor
#     else:
#         print('Saldo insuficiente')
#     return saldo
# def mostrarSaldo(saldo):
#     print(f'Seu saldo é de: {saldo}')




# while True:
#     opcao = input('1 - Depositar\n2 - Sacar\n3 - Mostrar Saldo\n4 - Sair\n')
#     if opcao == '4':
#         print('Saindo...')
#         break
#     elif opcao == '1':
#         saldo = depositar(saldo)#1000
#     elif opcao == '2':
#         saldo = sacar(saldo)
#     elif opcao == '3':
#         mostrarSaldo(saldo)


# Utilizando POO

# class ContaBancaria:
#     def __init__(self,saldo = 0,nome = ''):
#         self.saldo = saldo
#         self.nome = nome
#     def depositar(self,valor):
#         self.saldo += valor
#         print(f'Valor depositado com sucesso, seu novo saldo é: {self.saldo}')
#     def sacar(self, valor):
#         if valor <= self.saldo:
#             self.saldo -= valor
#         else:
#             print('Você não possui saldo suficiente')
#     def mostrarSaldo(self):
#         print(f'Seu saldo é: {self.saldo}')
        

# conta1 = ContaBancaria(1200,'João')
# while True:
#     opcao = input('1 - Depositar\n2 - Sacar\n3 - Mostrar Saldo\n4 - Sair\n')
#     if opcao == '4':
#         print('Saindo...')
#         break
#     elif opcao == '1':
#         valor = float(input('Digite o valor a ser depositado: '))
#         conta1.depositar(valor)
#     elif opcao == '2':
#         valor = float(input('Digite o valor a ser sacado: '))
#         conta1.sacar(valor)
#     elif opcao == '3':
#         conta1.mostrarSaldo()

# Crie uma classe que represente um carro, com atributos como marca, ano e modelo, velocidade, e métodos como ligar (mostrar uma mensagem avisando que o carro está ligado), desligar (mostrar uma mensagem dizendo que o carro está desligado) acelerar (deve acrescentar 10 na velocidade) e frear (deve reduzir 10 na velocidade).

# class Carro:
#     def __init__(self,marca = '',ano = 0, modelo = '', velocidade = 0):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.velocidade = velocidade
#     def ligar():
#         print('O carro está ligado')
#     def desligar():
#         print('O carro está desligado')
#     def acelerar(self):
#         self.velocidade += 10
#     def frear(self):
#         if self.velocidade >=10:
#             self.velocidade -= 10
#         else:
#             print('O carro está parado')


# carro1 = Carro('Fiat',2023,'Argo',20)

# print(carro1.velocidade)
# carro1.acelerar()

# print(carro1.velocidade)

# carro1.frear()
# carro1.frear()
# carro1.frear()
# carro1.frear()
# print(carro1.velocidade)

# print(carro1.modelo)

# carro1.velocidade = -10

# print(carro1.velocidade)

# class ContaBancaria:
#     def __init__(self,saldo = 0,nome = ''):
#         self.__saldo = saldo
#         self.nome = nome

#     def depositar(self,valor):
#         self.__saldo += valor
#         print(f'Valor depositado com sucesso, seu novo saldo é: {self.__saldo}')

#     def sacar(self, valor):
#         if valor <= self.__saldo:
#             self.__saldo -= valor
#         else:
#             print('Você não possui saldo suficiente')
#     def mostrarSaldo(self):
#         print(f'Seu saldo é: {self.__saldo}')
    


# conta1 = ContaBancaria(1500,'Ana')
# conta1.mostrarSaldo()
# print(conta1.__saldo)


## Pilar do Encapsulamento



# class Produto:
#     def __init__(self,nome, preco):
#         self.nome = nome
#         self.__preco = preco
#     #Criando os getters
#     def get_preco(self):
#         return self.__preco
    
#     #Criando os setters
#     def set_preco(self,novoPreco):
#         if novoPreco > 0:
#             self.__preco = novoPreco
#         else:
#             print('Preço inválido')


# class Produto:
#     def __init__(self,nome, preco):
#         self.nome = nome
#         self.__preco = preco
#     #Criando os getters
#     @property
#     def preco(self):
#         return self.__preco
    
#     @preco.setter
#     def preco(self,novoPreco):
#         if novoPreco > 0:
#             self.__preco = novoPreco
#         else:
#             print('Preço inválido')

# produto1 = Produto('Celular',1500)

# print(produto1.preco)

# produto1.preco = 1000

# print(produto1.preco)

# produto1.preco = -1000

# print(produto1.preco)

## Pilar da Herança

class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def exibirDados(self):
        print(f'Nome: {self.nome}, Salario: R${self.salario}')        

class Gerente(Funcionario):
    def __init__(self, nome, salario,bonos):
        super().__init__(nome, salario)
        self.bonos = bonos
    def mostrarBonos(self):
        print(f'O bonos é: {self.bonos}')

gerente1 = Gerente('João',2500,1500)
gerente1.exibirDados()
gerente1.mostrarBonos()