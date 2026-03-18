# maior e menor pesos lidos

pesos = []

for c in range(1,6):
    while True:
        try:
            peso = int(input('qual seu peso? '))
            break
        except ValueError:
            print('digite um numero inteiro')
    pesos.append(peso)
pesos.sort()
print(min(pesos), max(pesos))
