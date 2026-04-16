#Crie um sistema de menu no terminal com as opções:
#1 - Listar funcionários
#2 - Adicionar funcionário
#3 - Atualizar salário
#4 - Deletar funcionário
#0 - Sair

def menu():
    print('-='*16)
    print('''[1] - Listar funcionários
[2] - Adicionar funcionário
[3] - Atualizar salário
[4] - Deletar funcionário
[0] - Sair''')
    print('-=' * 16)
def escolha():
    try:
        escolha = int(input())
        return escolha
    except ValueError:
        print('Digite um numero valido')
def lista():
    pass
menu()

