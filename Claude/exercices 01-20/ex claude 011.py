# dicionarios e def

produto1 = {'produto':'Notebook','preco':4000,'estoque':50}
produto2 = {'produto':'smartphone','preco':10500,'estoque':100}
produto3 = {'produto':'Televisao','preco':3000,'estoque':10}

def exibir_produto(x):
    print(f'''\nProduto: {x['produto']}
Preco: {x['preco']}
Estoque: {x['estoque']}
''')

exibir_produto(produto1)
exibir_produto(produto2)
exibir_produto(produto3)