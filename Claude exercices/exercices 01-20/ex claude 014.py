# controle de vendas

def cadastrar_venda(vendedor, produto, valor):
    venda = {'vendedor': vendedor, 'produto': produto, 'valor': valor}
    return venda
def total_por_vendedor(lista_vendas, nome):
    soma = 0
    for venda in lista_vendas:
        if venda['vendedor'] == nome:
            soma += venda['valor']
    return soma
def maior_venda(lista_vendas):
    venda_maxima = 0
    dic_venda_maxima = {}
    for venda in lista_vendas:
        if venda['valor'] > venda_maxima:
            venda_maxima = venda['valor']
            dic_venda_maxima = venda
    return dic_venda_maxima

def resumo(lista_vendas):
    nomes_printados = []
    print()
    for venda in lista_vendas:
        print(f'Vendedor: {venda['vendedor']:<10} Produto: {venda['produto']:<10} Valor: R$ {venda['valor']:>8.2f}')
    print()
    for venda in lista_vendas:
        vendedor = venda['vendedor']
        if vendedor not in nomes_printados:
            print(f'Total de vendas do(a) {venda['vendedor']}: R$ {total_por_vendedor(lista_vendas, vendedor):.2f}')
            nomes_printados.append(vendedor)
    venda_do_dia = maior_venda(lista_vendas)
    print()
    print(f'A maior venda do dia foi de R$ {venda_do_dia['valor']:.2f} vendida por {venda_do_dia['vendedor']}')

venda1 = cadastrar_venda('Ana', 'Notebook', 3200.00)
venda2 = cadastrar_venda('Carlos','Mouse',150.00)
venda3 = cadastrar_venda('Ana','Teclado',280.00)
venda4 = cadastrar_venda('Maria','Monitor',1100.00)
venda5 = cadastrar_venda('Carlos','Notebook',3200.00)
venda6 = cadastrar_venda('Maria','Headset',420.00)

vendas = [venda1, venda2, venda3, venda4, venda5, venda6]

resumo(vendas)