# EXERCICIO 1------------------------------------------------------------

# Entrada de dados do usuário.
nmr = int(input("Escolha um numero: "))

# Estrutura para verificar se o numero é positivo, negativo ou zero
if (nmr > 0):
    print("Seu numero é positivo.")
elif(nmr == 0):
    print("Seu numero é o zero.")
else:
    print("Seu numero é negativo.")

# EXERCICIO 2-----------------------------------------------------------

# Exibe as opções para o usuário.
print("Menu dos dias das semanas: ")
print("1 - Domingo.")
print("2 - Segunda-Feira.")
print("3 - Terça-Feira.")
print("4 - Quarta-Feira.")
print("5 - Quinta-Feira.")
print("6 - Sexta-Feira.")
print("7 - Sabado.")

# Entrada de dados do usuário.
escolha = int(input("Digite um numero de 1 a 7: "))

match escolha:
    case 1: print("Você escolheu Domingo (Fim de semana).")
    case 2: print("Você escolheu Segunda (Dia util).")
    case 3: print("Você escolheu Terça (Dia util).")
    case 4: print("Você escolheu Quarta (Dia util).")
    case 5: print("Você escolheu Quinta (Dia util).")
    case 6: print("Você escolheu Sexta (Dia util).")
    case 7: print("Você escolheu Sabado (Fim de semana).")
    case _: print("ERRO.")

# EXERCICIO 3-----------------------------------------------------------

# Entrada de dados do usuário.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um segundo numero: "))

# Execução do operador ternario para verificar se os numeros sao divisiveis.
resultado = 'Sim os numeros sao divisiveis' if n1 % n2 == 0 else 'Os numeros nao sao divisiveis'
print(resultado)

# EXERCICIO 4-----------------------------------------------------------

print("Menu dos meses: ")
print("1 - Janeiro.")
print("2 - Fevereiro.")
print("3 - Março.")
print("4 - Abril.")
print("5 - Maio.")
print("6 - Junho.")
print("7 - Julho.")
print("8 - Agosto.")
print("9 - Setembro.")
print("10 - Outubro.")
print("11 - Novembro.")
print("12 - Dezembro.")

# Entrada de dados do usuário.
escolha = int(input("Digite um numero de 1 a 12 para escolher um mês: "))

match escolha:
    case 1: print("Você escolheu Janeiro (31 dias).")
    case 2: print("Você escolheu Fevereiro (28 dias).")
    case 3: print("Você escolheu Março (31 dias).")
    case 4: print("Você escolheu Abril (30 dias).")
    case 5: print("Você escolheu Maio (31 dias).")
    case 6: print("Você escolheu Junho (30 dias).")
    case 7: print("Você escolheu Julho (31 dias).")
    case 7: print("Você escolheu Agosto (31 dias).")
    case 7: print("Você escolheu Setembro (30 dias).")
    case 7: print("Você escolheu Outubro (31 dias).")
    case 7: print("Você escolheu Novembro (30 dias).")
    case 7: print("Você escolheu Dezembro (31 dias).")
    case _: print("ERRO.")

# EXERCICIO 5-----------------------------------------------------------

# Entrada de dados do usuário.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um segundo numero: "))
n3 = int(input("Digite um terceiro numero: "))

if (n1 > n2 and n3):
    print(f"O numero {n1} é o maior")
elif (n2 > n1 and n3):
    print(f"O numero {n2} é o maior")
else:
    print(f"O numero {n3} é o maior")


# EXERCICIO 6-----------------------------------------------------------

# Entrada de dados do usuário.
idade = int(input("Digite sua idade: "))

# Estrutura para verificar a classificação de idade.
if (idade <= 12):
    print(f"Sua idade, {idade}, classifica em Criança - 0 a 12 anos.")
elif (idade <= 17):
    print(f"Sua idade, {idade}, classifica em Adolescente - 13 a 17 anos.")
elif (idade <= 59):
    print(f"Sua idade, {idade}, classifica em Adulto - 18 a 59 anos..")   
else:
    print(f"Sua idade, {idade}, classifica em Idoso - 60 anos ou mais..")