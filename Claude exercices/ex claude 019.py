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


placar = [
    {'nome':'Mocotó', 'pontuacao': 2000},
    {'nome':'Tiago', 'pontuacao': 2500},
    {'nome':'Mari', 'pontuacao': 1750},
    {'nome':'Juliana', 'pontuacao': 3000}
]

while True:
    try:
        texto = carregar_dados()
        if texto:
            print('\nTabela do torneio\n')
            for i in range(0, len(texto)):
                print(f'Nome: {texto[i]['nome']:<10} Pontuação: {texto[i]['pontuacao']}')
            break
        else:
            salvar_dados(placar)
    except FileNotFoundError:
        salvar_dados(placar)