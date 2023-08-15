# Coleta de dados do usuário.
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
email = input("Digite seu email: ")

# Cria ou abre um arquivo pro usuário
arquivo = open(file="usuario.txt", mode="w+", encoding="utf8")

# Grava as informações do usúario no txt.
dados = []
dados.append(f"Nome: {nome}\n")
dados.append(f"Idade: {idade}\n")
dados.append(f"Email: {email}\n")

arquivo.writelines(dados)

# Encerra a gravação do conteúdo
arquivo.close()