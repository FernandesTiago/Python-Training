# taboada usando for in range

while True:
    try:
        n = input('Qual a taboada que deseja? ')
        n = int(n)
        if 0 < n <= 10:
            break
        else:
            print('Deve ser um valor de 0 a 10')
    except ValueError:
        print('Deve ser um valor de 0 a 10')

for c in range(1,11):
    print(n * c)
