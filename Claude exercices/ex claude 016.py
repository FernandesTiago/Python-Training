# started using files

def att_float(list, x):
    for i in range(x, len(list)):
        list[i] = float(list[i])
    return list

with open('dados.txt', 'r') as arquivo:
    lista = arquivo.readlines()
    primeira_linha = lista[0].split()

    att_float(primeira_linha, 1)

    print(primeira_linha)