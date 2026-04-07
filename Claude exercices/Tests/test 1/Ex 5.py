# Sistema de cadastro de contatos com arquivo .txt
#
# Crie um programa com 3 funções:
#
# 1. salvar_contato(nome, telefone)
#    → Adiciona um contato no arquivo 'contatos.txt'
#    → Formato de cada linha: "nome;telefone"
#
# 2. listar_contatos()
#    → Lê o arquivo e imprime todos os contatos assim:
#    → Nome: Ana | Telefone: 99999-0000
#    → Trate o caso do arquivo não existir
#    → Trate o caso do arquivo estar vazio
#
# 3. buscar_contato(nome)
#    → Lê o arquivo e retorna o telefone do contato
#    → Se não encontrar, retorna None
#    → Trate o caso do arquivo não existir
#
# Teste chamando as 3 funções no final

def limpar_arquivo():
    with open('contatos.txt','w'):
        pass

def salvar_contato(nome, telefone):
    """ADICIONA CONTATO NO ARQUIVO"""
    with open('contatos.txt','a') as arquivo:
        arquivo.write(f'{nome};{telefone}\n')

def listar_contatos():
    try:
        with open('contatos.txt','r') as arquivo:
            texto = arquivo.readlines()
            if texto:
                print('\nLista de contatos:\n')
                for i in range(0, len(texto)):
                    texto[i] = texto[i].split(';')
                    numero = texto[i][1]
                    numero = list(numero.replace('\n',''))
                    numero.insert(5,'-')
                    numero = ''.join(numero)
                    print(f'Nome: {texto[i][0]:<10} | Telefone: {numero}')
                print()
            else:
                print('Lista vazia')
    except FileNotFoundError:
         with open('contatos.txt','a') as arquivo:
             pass
         print('lista vazia')

def buscar_contato(nome):
    try:
        with open('contatos.txt','r') as arquivo:
            texto = arquivo.readlines()
            print('Buscar contatos:\n')
            teste = 0
            if texto:
                for i in range(0, len(texto)):
                    texto[i] = texto[i].split(';')
                    if texto[i][0] == nome:
                        numero = texto[i][1]
                        numero = list(numero.replace('\n',''))
                        numero.insert(5,'-')
                        numero = ''.join(numero)
                        return numero
            else:
                print('Lista vazia')
    except FileNotFoundError:
         with open('contatos.txt','a') as arquivo:
             pass
         print('lista vazia')


salvar_contato('Tiago','999380440')
salvar_contato('Juliana','991713132')

listar_contatos()

numero = buscar_contato('Tiago')
print(numero)

limpar_arquivo()