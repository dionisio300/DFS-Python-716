'''
================================================================
Questões básicas:


1️. Criar uma Classe Carro 
Crie uma classe Carro com os atributos marca, modelo e ano. Adicione um 
método exibir_dados() que retorna os detalhes do carro. 

2️. Criar uma Classe Funcionario 
Crie uma classe Funcionario com os atributos nome e salario. Adicione um 
método aumentar_salario(percentual). 

3️. Criar um sistema de Cadastro de Usuários 
Crie uma classe Usuario com nome e senha. O atributo senha deve ser privado e 
acessível apenas por um método verificar_senha(). 

4️. Criar um sistema de Animais com Herança 
Crie uma hierarquia de classes para representar diferentes tipos de animais, cada 
um com seu próprio método emitir_som(). 


==================================================================
Questões avançadas:


Questão 1️: Sistema de Controle de Estoque para uma Loja       
Requisitos do sistema: 
1. Criar uma classe Produto, com os seguintes atributos: 
o nome (string) 
o preco (float) 
o quantidade_estoque (int) 
2. Criar métodos na classe Produto: 
o vender(quantidade): diminui a quantidade em estoque. Se não 
houver estoque suficiente, exibe uma mensagem de erro. 
o repor(quantidade): adiciona produtos ao estoque. 
o exibir_info(): retorna uma string com as informações do produto. 
3. Criar classes derivadas de Produto para diferentes tipos de produtos: 
o Eletronico (adiciona o atributo garantia_meses) 
o Alimento (adiciona o atributo data_validade) 
4. Criar uma classe Loja, que gerencia os produtos no estoque: 
o A loja deve armazenar os produtos em uma lista chamada estoque. 
o Deve ter um método adicionar_produto(produto). 
o Deve ter um método exibir_estoque(), que lista todos os produtos 
disponíveis. 
5. Criar um menu interativo que permita ao usuário: 
   Cadastrar novos produtos no estoque 
   Vender produtos 
   Repor produtos 
   Exibir o estoque da loja 





Gabarito
'''
class Produto():
    def __init__(self,nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def vender(self,qtdVenda):
        if self.quantidade >= qtdVenda:
            self.quantidade -= qtdVenda
            #self.quantidade = self.quantidade - qtdVenda
        else:
            print(f'A quantidade disponível não é suficiente, temos apenas {self.quantidade} unidades')
    def repor(self,qtdRepor):
        self.quantidade += qtdRepor
        return self.quantidade
    def exibir_info(self):
        print(f'Nome: {self.nome}, Preço: {self.preco}, quantidade em estoque: {self.quantidade}')

# 3. Criar classes derivadas de Produto para diferentes tipos de produtos: 
# o Eletronico (adiciona o atributo garantia_meses) 
# o Alimento (adiciona o atributo data_validade) 
class Eletronicos(Produto):
    def __init__(self, nome, preco, quantidade,garantia_meses):
        super().__init__(nome, preco, quantidade)
        self.garantia_meses = garantia_meses
    def estenderGarantia(self):
        self.garantia_meses += 12


class Alimento(Produto):
    def __init__(self, nome, preco, quantidade,data_validade):
        super().__init__(nome, preco, quantidade)
        self.data_validade = data_validade


# 4. Criar uma classe Loja, que gerencia os produtos no estoque: 
# o A loja deve armazenar os produtos em uma lista chamada estoque. 
# o Deve ter um método adicionar_produto(produto). 
# o Deve ter um método exibir_estoque(), que lista todos os produtos 
# disponíveis. 

class Loja():
    def __init__(self,estoque):
        self.estoque = estoque

    def adicionar_produto(self,produto):
        self.estoque.append(produto)
    def exibir_estoque(self):
        for prod in self.estoque:
            prod.exibir_info()

produto1 = Produto('Monitor',600,10)
# produto1.vender(6)
# print(produto1.quantidade)
# print(produto1.repor(20))

# produto1.exibir_info()

eletronico1 = Eletronicos('Celular',1500,20,12)

# eletronico1.vender(2)
# eletronico1.estenderGarantia()
# print(eletronico1.quantidade)
# print(eletronico1.garantia_meses)


alimento1 = Alimento('Arroz',6,100,'20/12/2026')
# print(f'O {alimento1.nome} custa {alimento1.preco} e tem validade até {alimento1.data_validade}')

# produtos = [produto1,eletronico1,alimento1]

# loja1 = Loja(produtos)
# loja1.exibir_estoque()

# loja1.adicionar_produto(Alimento('Café',12,50,'20/02/2027'))
# loja1.exibir_estoque()

# 5. Criar um menu interativo que permita ao usuário: 
#    Cadastrar novos produtos no estoque 
#    Vender produtos 
#    Repor produtos 
#    Exibir o estoque da loja 

produtos = [produto1,eletronico1,alimento1]
loja1 = Loja(produtos)

while True:
    opcao = input('Digite uma opção:\n1 - Cadastrar Produto\n2 - Vender\n3 - Repor\n4 - Exibir Estoque\n5 - Sair\n')
    if opcao == '5':
        print('Saindo...')
        break
    if opcao == '1':
        tipoProduto = input('1 - Alimento\n2 - Eletronico\n3 - Produto')
        if tipoProduto == '1':
            nome = input('Digite o nome do produto: ')
            preco = float(input('Digite o preço do produto: '))
            quantidade = int(input('Digite a quantidade: '))
            validade = input('Digite a validade "DD/MM/AAAA": ')
            alimento1 = Alimento(nome,preco,quantidade,validade)
            loja1.adicionar_produto(alimento1)
            print('Produto cadastrado com sucesso!!')
        if tipoProduto == '2':
            nome = input('Digite o nome do produto: ')
            preco = float(input('Digite o preço do produto: '))
            quantidade = int(input('Digite a quantidade: '))
            garantia = int(input('Digite a garantia em meses: '))
            eletronico1 = Eletronicos(nome,preco,quantidade,garantia)
            loja1.adicionar_produto(eletronico1)
            print('Produto cadastrado com sucesso!!')
        if tipoProduto == '3':
            nome = input('Digite o nome do produto: ')
            preco = float(input('Digite o preço do produto: '))
            quantidade = int(input('Digite a quantidade: '))
            
            produto1 = Produto(nome,preco,quantidade)
            loja1.adicionar_produto(produto1)
            print('Produto cadastrado com sucesso!!')

    if opcao == '2':
        nome = input('Digite o nome do produto vendido: ')

        for produto in produtos:
            if nome == produto.nome:
                qtdVenda = int(input(f'quantos {produto.nome} foram vendidos? '))
                produto.vender(qtdVenda)
                print('produto vendido com sucesso!!')
                break
    if opcao == '3':
        nome = input('Digite o nome do produto Reposto: ')

        for produto in produtos:
            if nome == produto.nome:
                qtdVenda = int(input(f'quantos {produto.nome} foram repostos? '))
                produto.repor(qtdVenda)
                print('Estoque reposto com sucesso!!')
                break
    if opcao == '4':
        loja1.exibir_estoque()


'''
Questão 2️: Sistema de Gestão Escolar          
Requisitos do sistema: 
1. Criar uma classe Pessoa, com os atributos: 
o nome (string) 
o idade (int) 
2. Criar uma classe Aluno que herda de Pessoa, adicionando: 
o matricula (string) 
o notas (lista de floats) 
o Métodos:  
▪ adicionar_nota(nota): adiciona uma nova nota ao aluno. 
▪ calcular_media(): retorna a média das notas. 
▪ exibir_info(): exibe as informações do aluno. 
3. Criar uma classe Professor que herda de Pessoa, adicionando: 
o disciplina (string) 
o turma (string) 
o exibir_info(): exibe os dados do professor. 
4. Criar uma classe Escola, que gerencia alunos e professores: 
o Lista de alunos e professores. 
o Métodos para cadastrar novos alunos e professores. 
o Método exibir_pessoas(), que exibe todos os alunos e professores 
cadastrados. 
5. Criar um menu interativo permitindo:    Cadastrar alunos e professores 
   Adicionar notas para os alunos 
   Listar todos os alunos e professores 
   Calcular e exibir a média de um aluno específico 
'''






