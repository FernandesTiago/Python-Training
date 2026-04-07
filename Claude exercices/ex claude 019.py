import json

def carregar_dados():
    """RETORNA OS DADOS DO JSON"""
    with open('dados19.json','r') as arquivo:
        dados = json.load(arquivo)
        return dados
    
def salvar_dados(dados):
    """SALVA OS DADOS () NO ARQUIVO"""
    with open('dados19.json','w') as arquivo:
        json.dump(dados, arquivo)

def deletar_dados():
    """DELETA A LISTA COMPLETA"""
    with open('dados19.json','w'):
        pass

def printar(txt):
    """PRINTA A LISTA DE MANEIRA ORGANIZADO"""
    texto = sorted(txt, key=lambda x: x['pontuacao'], reverse=True)
    for i in range(0, len(texto)):
        print(f'Nome: {texto[i]['nome']:<10} Pontuação: {texto[i]['pontuacao']}')

placar = [
    {'nome':'Mocotó', 'pontuacao': 2000},
    {'nome':'Tiago', 'pontuacao': 2500},
    {'nome':'Mari', 'pontuacao': 1750},
    {'nome':'Juliana', 'pontuacao': 3000}
]

while True:
    try:
        texto = carregar_dados()
        print('\nTabela do torneio\n')
        printar(texto)
        break
    except (FileNotFoundError, json.JSONDecodeError):
        salvar_dados(placar)

while True:
    adicionar = input('Deseja adicionar um novo jogador? (S/N/D) ').strip().title()
    if adicionar == 'S':
        jogador = input('Qual o nome do jogador? ').title().strip()
        while True:
            try:
                pontuacao = int(input('Qual a pontuacao? '))
                break
            except ValueError:
                print('Digite um numero inteiro!')
        dic_jogador = {'nome': jogador, 'pontuacao': pontuacao}
        texto.append(dic_jogador)
        print('\nTabela do torneio\n')
        printar(texto)
        salvar_dados(texto)
        break
    elif adicionar == 'D':
        deletar_dados()
        break
    elif adicionar == 'N':
        print('Nada adicionado!')
        break
    else:
        print('Digite S, N ou D!!')
