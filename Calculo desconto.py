valor = float(input("Digite o valor total da compra: R$ "))

if valor < 200:
    desconto = 0.05
elif valor >= 200 and valor < 300:
    desconto = 0.10
else:
    desconto = 0.15

valor_desconto = valor * desconto
total_pagar = valor - valor_desconto

print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {total_pagar:.2f}")