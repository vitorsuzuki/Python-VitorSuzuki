# Declaração de um procedimento sem parâmetro.
def boas_vindas():
    print("Seja bem vindo ao software")

# Chamada de um procedimento sem parâmetro.
boas_vindas()

# Declaração de um procedimento com parâmetro.
def boas_vindas2(nome="Usuario não definido"):
    print(f"Sja bem vindo {nome} ao software")

# Chamada de um procedimento com parâmetro.
boas_vindas2("Vitor Suzuki")