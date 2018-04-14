# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Convertendo um número octal em um número decimal
soma = 0
numero = raw_input()
for i in range(len(numero)):
	resultado = int(numero[i]) * 8 ** (len(numero) - 1 - i)
	soma += resultado
	print "%s * 8^%d = %d" %(numero[i],len(numero)-1-i,resultado)

print "%s(8) = %d(10)" %(numero,soma)
