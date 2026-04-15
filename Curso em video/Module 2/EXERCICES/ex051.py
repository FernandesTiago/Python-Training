# Progressao aritimetica

while True:
    try:
        pt = int(input('qual o primeito termo? '))
        break
    except ValueError:
        print('digite um numero inteiro')
while True:
    try:
        razao = int(input('qual a razao? '))
        break
    except ValueError:
        print('digite um numero inteiro')

for c in range(pt, pt+razao*10, razao):
    print(c)