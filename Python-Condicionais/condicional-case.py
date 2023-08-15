# Exibe as opções para o usuário.
print("Menu de funções do Software: ")
print("1 - Cadastrar novo usuário.")
print("2 - Editar registros do usuário.")
print("3 - Apagar registros do usuário.")
print("Para sair do menu digite qualquer tecla!!")

# Entrada de dados do usuário.
escolha = int(input("Digite a opção desejada: "))

match escolha:
    case 1: print("Você escolheu cadastrar um novo usuário.")
    case 2: print("Você escolheu editar as informações de um usuário.")
    case 3: print("Você escolheu deletar os registros de um usuário.")
    case _: print("Você escolheu sair do menu.")