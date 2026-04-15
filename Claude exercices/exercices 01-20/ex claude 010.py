# desconto def

def valor_descontado(a, b=0):
    print(f'O valor do produto eh de {a - a * b/100:.2f}')

# nao estou usando as verificacoes de input que geralmente uso pois estou apenas explorando o def
valor = int(input('qual o valor do produdo? '))
desconto = int(input('qual o desconto? (0%-100%) '))
valor_descontado(valor, desconto)
