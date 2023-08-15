# Função que calcula a área de um retangulo.
def area(base=0, altura=0):
    resultado = base * altura
    return resultado

# Chamada nomeada da função.
area = area(base=8, altura=5)

# Exibe a saída da função.
print(f"A área do retângulo é {area} metros quadrados")