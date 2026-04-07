# Crie uma função que recebe uma lista de números
# e retorna a soma de todos os elementos.

# Teste com: [10, 20, 30, 40]

def soma(lista_numeros):
    soma = 0
    for numero in lista_numeros:
        soma += numero
    return soma

lista = [10, 20, 30, 40]

print(f'Soma = {soma(lista)}')