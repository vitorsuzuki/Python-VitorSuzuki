# Recebe o nome do usuário.
nome = input("Informe seu nome: ")

# Recebe a idade do usuário.
idade = int(input("Informe sua idade: "))

# Formatação de strings (F-STRINGS).
# Exemplo de saída sem formatação.
print("Seja bem-vindo", nome, "de", idade, "anos...")

# Exemplo de saída com formatação.
print(f"Seja bem-vindo {nome} de {idade} anos...")

# Função PRINT com o parâmetro END.
print("Hello", "World", end="\n")

# Função PRINT com o parâmetro SEP
print("O", "Python", "é", "legal", sep="-")