# Exercicio 1------------------------------------------------------

# Tenta realizar a execução do codigo
try:
    # Função para o calculo do quadrado.
    def quadrado(n1=0):
        resultado = n1*n1
        return resultado

    # Coleta de dados do usuario.
    n1 = int(input("Digite um numero: "))

    quadrado = quadrado(n1=n1)
    print(f"O quadrado do numero é: {quadrado}")

# Captura o erro de formato de dado.
except ValueError:
    print("O formato de dado informado é inválido")

# Captura um erro inesperado.
except Exception:
    print("Um erro inseperado foi encontrado.")

# Exercicio 2 ------------------------------------------------------

# Tenta realizar a execução do codigo
try:
    # Função para o calculo da divisão.
    def div(divisor=0, dividendo=0):
        resultado = divisor/dividendo
        return resultado

    # Coleta dos dados do usuario.
    divisor = int(input("Digite um numero para o divisor: "))
    dividendo = int(input("Digite um numero para o dividendo: "))

    div = div(divisor=divisor, dividendo=dividendo)
    print(f"O resultado da divisão é: {div}")

# Captura o erro da divisão por zero.
except ZeroDivisionError:
    print("Não é possivel dividir por zero.")

# Captura o erro inesperado.
except Exception:
    print("Um erro inseperado foi encontrado.")

# Exercicio 3 ------------------------------------------------------

# Tenta realizar a execução do codigo
try:
    # Função para juntar as frases
    def juntar(plv1="", plv2=""):
        print(plv1, plv2)
        return juntar

    # Coleta de dados do usuario.
    plv1 = str(input("Escreva a primeira frase: "))
    plv2 = str(input("Escreva a segunda frase: "))

    # Junta as palavras
    juntar = juntar(plv1=plv1, plv2=plv2)

# Captura o erro de formato de dado.
except ValueError:
    print("O formato de dado informado é inválido")

# Captura o erro inesperado.
except Exception:
    print("Um erro inseperado foi encontrado.")