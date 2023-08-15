# Exercicio 1 -----------------------------------------------------

# Entrada de dados do usuario.
celsius = int(input("Selecione um numero para a conversão de celisus para Fahrenheit: "))

# Função que calcula a conversão.
def farh():
    resultado = (celsius * 9/5) + 32
    return resultado

# Chamada nomeada da função.
farh = farh()

# Exibe a saída da função.
print(f"A conversão para Fahrenheit é: {farh} ")

# Exercicio 2 -----------------------------------------------------

# Entrada de dados do usuario.
nmr = float(input("Selecione um numero para a conversão de Celsius para Kelvin: "))

# Função que calcula a conversão.
def kelvin():
    resultado = nmr + 273.15
    return resultado

# Chamada nomeada da função.
kelvin = kelvin()

# Exibe a saída da função.
print(f"A conversão para Kelvin é: {kelvin} ")

# Exercicio 3 -----------------------------------------------------

# Entrda de dados do usuario.
n1 = int(input("Selecione um numero:"))
n2 = int(input("Selecione um segundo numero:"))
n3 = int(input("Selecione um terceiro numero:"))

# Função que calcula a media aritmetica.
def calc():
    media = n1 + n2 + n3 / 3
    return media

# Chamada nomeada da função.
calc = calc()

# Exibe a saída da função.
print(f"A media dos numeros é {calc}")

# Exercicio 4 -----------------------------------------------------

# Função de adição.
def adi(n1=0,n2=0):
    resultado = n1 + n2
    return resultado

# Função de SUBTRAÇÃO.
def sub(n1=0,n2=0):
    resultado = n1 - n2
    return resultado

# Função de MULTIPLICAÇÃO.
def mult(n1=0,n2=0):
    resultado = n1 * n2
    return resultado

# Função de DIVISÃO.
def div(n1=0,n2=0):
    resultado = n1 / n2
    return resultado

# Entrda de dados do usuario.
n1 = int(input("Selecione um numero:"))
n2 = int(input("Selecione um segundo numero:"))

# Exibe as operações disponiveis.
print("Menu das operações matematicas:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Entrada de dados do usuário.
escolha = int(input("Digite a opção desejada: "))

match escolha:
    case 1: print(f"O resultado da soma é {adi(n1, n2)}")
    case 2: print(f"O resultado da subtração é {sub(n1, n2)}")
    case 3: print(f"O resultado da multiplicação é {mult(n1, n2)}")
    case 4: print(f"O resultado da divisão é {div(n1, n2)}")
    case _: print("ERRO")


# Exercicio 5 -----------------------------------------------------

# Declaração de um procedimento com parâmetro.
def cnh(idade=0,minima=0):
    if (idade < minima):
        print("Não podera tirar carteira")
    else:
        print("Apto para tirar carteira de CARRO e MOTO.")

# Entrada dos dados do usuario.
idade = int(input("Qual é a sua idade: "))

# Menu de opções.
print("Categoria de CNH:")
print("1 - (A) - Carro e Moto.")
print("2 - (C, D ou E - Caminhões e Ônibus.)")
escolha1 = int(input("Digite a opção desejada: "))

# Correspondencia
match escolha1:
    case 1: cnh(idade=idade, minima=18)
    case 2: cnh(idade=idade, minima=21)
