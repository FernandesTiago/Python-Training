# estoque usando def

def cadastrar_produto(nome, quantidade, preco):
    produto = {'nome': nome,'quantidade': quantidade, 'preco': preco}
    return produto

def valor_total_produto(produto):
    valor_total = produto['quantidade']*produto['preco']
    return valor_total

def valor_total_estoque(lista_produtos):
    valor_estoque_total = 0
    for produto in lista_produtos:
        valor_estoque_total += valor_total_produto(produto)
    return valor_estoque_total
def produtos_em_falta(lista_produtos):
    produtos_faltando = []
    for produto in lista_produtos:
        if produto['quantidade'] == 0:
            produtos_faltando.append(produto['nome'])
    return produtos_faltando
def printar(lista_produtos):
    faltando = produtos_em_falta(lista_produtos)
    for produto in lista_produtos:
        print(f'Produto: {produto['nome']:<10} Quantidade: {produto['quantidade']:>3} Preco: {produto['preco']:>6.2f}')
    print(f'Valor total do estoque: {valor_total_estoque(lista_produtos):.2f}')
    if len(faltando) == 0:
        print(f'Nenhum item faltando')
    else:
        print(f'Os item em falta sao: {', '.join(faltando)}')

produto1 = cadastrar_produto('Caneta', 50, 1.5)
produto2 = cadastrar_produto('Caderno', 0, 12.90)
produto3 = cadastrar_produto('Borracha', 30, 0.75)
produto4 = cadastrar_produto('Regua', 0, 3.20)
produto5 = cadastrar_produto('lapis', 100, 0.5)

produtos = [produto1, produto2, produto3, produto4, produto5]

printar(produtos)