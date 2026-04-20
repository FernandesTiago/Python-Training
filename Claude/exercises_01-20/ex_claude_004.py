# Criar cadastros de 3 produtos e exibir na tela ( usando listas e dicionarios )

produto1 = {'item': 'Computador','valor': 3500,'estoque': 4}
produto2 = {'item': 'Caixa de som','valor': 300,'estoque': 2}
produto3 = {'item': 'Televisao','valor': 5500,'estoque': 10}

listas = [produto1, produto2, produto3]

for lista in listas:
    print(f"Item: {lista['item']}", end=' ')
    print(f"Valor: {lista['valor']}", end=' ')
    print(f"Estoque: {lista['estoque']}")