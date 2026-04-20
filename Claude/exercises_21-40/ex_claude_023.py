# Class training

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def detalhes(self):
        print(f'Funcionario: {self.nome} | Salario: R$ {self.salario}')
    def __str__(self):
        return f'Funcionario: {self.nome} | Salario: R$ {self.salario}'
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
    def __str__(self):
        return f'Funcionario: {self.nome} | Salario: R$ {self.salario} | Departamento: {self.departamento}'
    
class Desenvolvidor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem
    def codar(self):
        if self.linguagem == 'Python':
            print(f'{self.nome}: print("Hello")')
        elif self.linguagem == 'Java':
            print(f'{self.nome}: System.out.println("Hello")')
        elif self.linguagem == 'JavaScript':
            print(f'{self.nome}: console.log("Hello")')

gerente = Gerente('Tiago', 2500, 'Cybersecurity')
dev1 = Desenvolvidor('Juliana', 1500, 'Python')
dev2 = Desenvolvidor('Mari', 1250, 'JavaScript')

devs = [dev1, dev2]
gerentes = [gerente]
funcionarios = gerentes + devs

for funcionario in funcionarios:
    funcionario.detalhes()

for dev in devs:
    dev.codar()