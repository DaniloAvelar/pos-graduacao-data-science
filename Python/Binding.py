def demonstrar_binding(numero, texto):
    """
    Função que recebe um número e uma string.
    Os nomes 'numero' e 'texto' são vinculados (bound) aos objetos
    passados como argumento no momento da chamada.
    """
    print(f"Valor do número: {numero} (ID na memória: {id(numero)})")
    print(f"Valor da string: {texto} (ID na memória: {id(texto)})")

# --- Testando a função ---

# Aqui, o literal 10 e a string "Python" são criados na memória.
# Os nomes 'meu_num' e 'minha_str' são vinculados a esses objetos.
meu_num = 10
minha_str = "Python"

print("--- Início do Programa ---")
demonstrar_binding(meu_num, minha_str)

# Exemplo de REBINDING:
# O nome 'meu_num' agora é vinculado a um NOVO objeto (20).
meu_num = 20
print("\n--- Após Rebinding de 'meu_num' ---")
print(f"Novo valor: {meu_num} (Novo ID: {id(meu_num)})")