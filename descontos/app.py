
print('=' * 36)
valor_compra = float(input('Digite o valor total da compra (R$): '))

# Divisor dos descontos para cada preço
if valor_compra < 200.00:
  taxa_desconto = 0.05 # desconto: 5%
elif valor_compra >= 200.00 and valor_compra < 300.00:
  taxa_desconto = 0.10 # desconto: 10%
else:
  taxa_desconto = 0.15 # desconto: 15%
  
# Calculo para o desconto
valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto

# Preço final apresentado ao cliente
print('=' * 36)
print(f'Você recebeu R${valor_desconto: .2f} de desconto!')
print(f'O produto que custava R${valor_compra: .2f} saiu por apenas R$ {valor_final: .2f}!')
print('=' * 36)
