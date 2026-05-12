nome = input("Qual é seu nome: ")
print(f"Prazer em te conhecer, {nome}!")
print("Prossiga com as instruções abaixo")

# Convertendo para inteiro
inteiro = int(input("Digite um número inteiro: "))

# Convertendo para flutuante (decimal)
flutuante = float(input("Digite um número de ponto flutuante: "))

# Convertendo para booleano
# Nota: Converter string para bool no Python é sutil.
# Se a string não estiver vazia, ela vira True.
entrada_bool = input("Digite um valor booleano (True ou False): ")
booleano = entrada_bool.strip().lower() == 'true'

print("\n--- Tipos de Dados Convertidos ---")
print(f"Inteiro: {type(inteiro)}")
print(f"Flutuante: {type(flutuante)}")
print(f"Booleano: {type(booleano)}")