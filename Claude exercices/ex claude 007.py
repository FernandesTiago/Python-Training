# global

x = 10
def minha_funcao():
    global x
    x = 20

minha_funcao()
print(x)  # agora sim vai printar 20