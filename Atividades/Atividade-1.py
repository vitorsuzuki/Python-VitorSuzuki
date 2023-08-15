# EXERCICIO 1.

# Coleta as informações.
n1 = int(input("informe um numero aleatorio: "))
n2 = int(input("informe um segundo numero aleatorio: "))

# Faz a diferença de qual é o maior ou menor e informa o resultado
if (n1 > n2):
    print(f"O numero {n1} é maior que o numero {n2}")
elif (n1 == n2):
    print(f"O numero {n1} é igual o numero {n2}")
else:
    print(f"O numero {n1} é menor que o numero {n2}")

# EXERCICIO 2.

# Coleta as informações.
celsius = int(input("Informe uma temperatura em celsius: "))

# Faz o calculo de conversão de celsius para fahrenheit
Fahrenheit = (celsius * 9/5) + 32
# Aprensenta o resultado
print(f"A conversão de {celsius} Celsius para Fahrenheit é {Fahrenheit} Fahrenheit")

# EXERCICIO 3.

# Coleta as informações.
ano = int(input("Informe um ano: "))

# Faz o calculo para identificar se o ano apresentado é bissexto ou não. E assim apresenta o resultado.
if (ano % 4 == 0):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")