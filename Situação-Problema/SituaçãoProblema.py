# Tenta realizar a execução do codigo
try:
    # Função que cria um arquivo de anotacão.
    def arq():
        with open(file="anotação.txt",mode="w", encoding="utf8") as arquivo:
            escrita = input("Escreva algo: ")
            arquivo.write(escrita)  
        return escrita

    # Função  para ler um arquivo de anotação.
    def arqleit():
        with open(file="anotação.txt",mode="r", encoding="utf8") as arquivo:
            # Lê o conteúdo do arquivo.
            conteudo = arquivo.read()
            # Exibe o conteúdo do arquivo.
            print(conteudo)
        return conteudo

    # Escrita das opções para o usúario.
    print("Escolha uma das opções:")
    print("1- Escreva um novo arquivo.")
    print("2- Ler um arquivo.")

    # Entrada de dados do usuário para escolher.
    escolha = int(input("Digite a opção: "))

    # Estrutura match-case das escolhas para o usúario.
    match escolha:
        case 1: print(f"Escolheu criar um novo arquivo: {arq()}")
        case 2: print(f"Escolheu ler um arquivo: {arqleit()}")
        case _: print("ERRO")

# Captura o erro de arquivo não encontrado.
except FileNotFoundError:
    print("Um arquivo não pode ser encontrado.")

# Captura o erro inesperado.
except Exception:
    print("Um erro inesperado ocorreu.")