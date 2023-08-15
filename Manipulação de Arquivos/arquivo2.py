# Cria ou tenta abrir um novo arquivo.
arquivo = open(file="frutas.txt", mode="w", encoding="utf8")

# Cria uma lista de frutas.
frutas = []
frutas.append("Banana\n")
frutas.append("Maçã\n")
frutas.append("Tomate\n")

# Graa o conteúdo no arquivo.
arquivo.writelines(frutas)

# Abre o arquivo para leitura.
arquivo = open(file="frutas.txt", mode="r", encoding="utf8")

conteudo = arquivo.read()

# Exibe o conteúdo do arquivo.
print(conteudo)

# Encerra a gravação do conteúdo
arquivo.close()