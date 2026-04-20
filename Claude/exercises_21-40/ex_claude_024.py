# cadastro de funcionario

import json

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def __str__(self):
        return f'Funcionario: {self.nome} | Salario: R$ {self.salario}'

def deletar_dados():
    with open('dados24.json', 'w') as arquivo:
        json.dump([], arquivo)

def printar():
    with open('dados24.json','r') as arquivo:
        texto = json.load(arquivo)
        print(f'Lista completa: {texto}')

def salvar_funcionario(funcionario):
    try:
        with open('dados24.json','r') as arquivo:
            texto = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print('Lista vazia')
        with open('dados24.json','w') as arquivo:
            texto = []
            json.dump(texto, arquivo)  
    else:
        with open('dados24.json', 'w') as arquivo:
            dic = {'nome': funcionario.nome, 'salario': funcionario.salario}
            texto.append(dic)
            json.dump(texto, arquivo)
        with open('dados24.json', 'r') as arquivo:
                texto = json.load(arquivo)


while True:
        try:
            printar()
            break
        except (FileNotFoundError, json.JSONDecodeError):
            print('Lista vazia')
            with open('dados24.json','w') as arquivo:
                texto = []
                json.dump(texto, arquivo)   

while True:                
    escolha = input('Deseja adicionar mais pessoas? (S,N,D) ').title().strip()
    if escolha == 'S':
        nome = input('Qual o nome? ')
        while True:
            try:
                salario = int(input('Qual o salario? '))
                break
            except ValueError:
                print('Digite um numero inteiro!')
        dev = Funcionario(nome,salario)
        salvar_funcionario(dev)
    elif escolha == 'N':
        break
    elif escolha == 'D':
        deletar_dados()
    else:
        print('Digite S, N ou D!')

printar()

with open('dados24.json', 'r') as arquivo:
    texto = json.load(arquivo)
    funcionarios = []
    for item in texto:
        obj = Funcionario(item['nome'], item['salario'])
        funcionarios.append(obj)
for funcionario in funcionarios:
    print(funcionario)
