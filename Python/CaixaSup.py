"""Você foi designado para criar um programa em Python para um caixa de supermercado. O programa deve solicitar ao cliente
a quantidade de cada produto adquirido e calcular o total da compra com base nos preços unitários dos itens.
Utilize os conceitos de atribuição, entrada e saída de dados para implementar o programa. """


print("=== SISTEMA DE CAIXA SUPERMERCADO ===")

# 1. Atribuição de Preços Unitários (Tabela de Preços)
preco_arroz = 25.50
preco_feijao = 8.90
preco_leite = 5.20

# 2. Entrada de Dados (Quantidade de cada item)
print("\nPor favor, informe a quantidade de cada item:")

# Convertendo para int pois a quantidade costuma ser um número inteiro
qtd_arroz = int(input(f"Arroz (R$ {preco_arroz}): "))
qtd_feijao = int(input(f"Feijão (R$ {preco_feijao}): "))
qtd_leite = int(input(f"Leite (R$ {preco_leite}): "))

# 3. Processamento (Cálculo do Total)
# O Python multiplica os valores e soma os resultados
total_arroz = qtd_arroz * preco_arroz
total_feijao = qtd_feijao * preco_feijao
total_leite = qtd_leite * preco_leite

valor_total_compra = total_arroz + total_feijao + total_leite

# 4. Saída de Dados (Cupom Fiscal Simples)
print("\n" + "="*30)
print("       CUPOM FISCAL")
print("="*30)
print(f"Arroz:   {qtd_arroz}x R$ {preco_arroz:.2f} = R$ {total_arroz:.2f}")
print(f"Feijão:  {qtd_feijao}x R$ {preco_feijao:.2f} = R$ {total_feijao:.2f}")
print(f"Leite:   {qtd_leite}x R$ {preco_leite:.2f} = R$ {total_leite:.2f}")
print("-" * 30)
print(f"TOTAL DA COMPRA: R$ {valor_total_compra:.2f}")
print("="*30)
print("Obrigado por comprar conosco!")