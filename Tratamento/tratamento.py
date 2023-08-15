# Tenta realizar a execução do codigo
try: 
    # Entrada de dados do usuário.
    dividendo = int(input("Informe o dividendo: "))
    divisor = int(input("Informe o divisor: "))

    # Realiza a divisão dos números.
    resultado = dividendo/divisor

    print(f"O resultado da divisão é: {resultado}")

# Captura o erro da divisão por zero.
except ZeroDivisionError:
    print("Não é possivel realizar a divisão por zero.")

# Captura o erro de formato de dado.
except ValueError:
    print("O formato de dado informado é inválido")

# Captura qualquer exceção.
except Exception:
    print("Um erro inesperado foi encontrado")