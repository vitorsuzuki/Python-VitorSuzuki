# Entrada de dados do usuario.
idade = int(input("informe sua idade: "))

# Estrutura condicional simples (IF-ELIF-ELSE).
if (idade < 12):
    print("Você é uma criança")
elif (idade <= 18):
    print("Você é um adolecente")
else:
    print("Você é adulto")