# Crie um dicionário representando um produto com as chaves:
# 'nome', 'preco', 'disponivel' (booleano)
#
# Depois imprima uma linha formatada assim:
# Produto: Teclado | Preço: R$ 150.00 | Disponível: Sim

produto = {'produto': 'Teclado', 'preço': 150, 'disponivel': True}

disponivel = produto['disponivel']
disponibilidade = 'Sim' if disponivel else 'Não'

print(f'Produto: {produto['produto']} | Preço: R$ {produto['preço']:.2f} | Disponivel: {disponibilidade}')