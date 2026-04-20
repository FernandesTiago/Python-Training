# Você tem esta lista de dicionários:
estoque = [
    {'nome': 'Caneta', 'qtd': 5},
    {'nome': 'Caderno', 'qtd': 12},
    {'nome': 'Borracha', 'qtd': 3}
]
# Ordene a lista por quantidade (menor pra maior) e imprima
# cada item assim:
# Caneta — 5 unidades



estoque = sorted(estoque, key=lambda x: x['qtd'], reverse=False)
# Nao vou mentir que aqui me confundi com o lambda, o x[1] como usei em outro exercicio nao funcionava 
# So cheguei a pesquisar por sem um fundamento novo que vi no ultimo exercicio e só usei uma vez, e vi que nesse caso posso usar o 
# nome da Key do dic


for i in range(0, len(estoque)):
    print(f'{estoque[i]['nome']} - {estoque[i]['qtd']} Unidades')