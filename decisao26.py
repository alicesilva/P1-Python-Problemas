#coding: utf-8
litros = float(raw_input())
tipo_combustivel = raw_input()

if tipo_combustivel[0] == "A":
	valor = litros * 1.90
	if litros <= 20:
		desconto = litros * 3
		valor_pago = valor - (desconto/100.0 * valor)
	elif litros > 20:
		desconto = litros * 5
		valor_pago = valor - (desconto/100.0 * valor)
else:
	valor = litros * 2.50
	if litros <= 20:
		desconto = litros * 4
		valor_pago = valor - (desconto/100.0 * valor)
	elif litros > 20:
		desconto = litros * 6
		valor_pago = valor - (desconto/100.0 * valor)

print valor_pago
