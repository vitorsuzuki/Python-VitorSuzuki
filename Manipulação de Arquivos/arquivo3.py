# Cria ou abre um arquivo de texto.
with open(file="carros.txt", mode="w+", encoding="utf8") as arquivo:

    # Grava o conteúdo no arquivo.
    arquivo.write("Opção 1: Opalão. \nOpção 2: Chevete. \nOpção 3: Fusca.")

# Cria ou abre um arquivo de texto.
with open(file="carros.txt", mode="r", encoding="utf8") as arquivo:

    # Lê o conteúdo do arquivo.
    conteudo = arquivo.read()

    # Exibe o conteúdo do arquivo.
    print(conteudo)
