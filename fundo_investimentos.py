# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Fundo de investimento

soma = 0
cont = 0

soma1 = 0
cont1 = 0

while True:
	quantia = float(raw_input())
	soma += quantia
	cont += 1
	media = float(soma) / cont
	if quantia < media:
		break
	soma1 += quantia
	cont1 += 1
	
print "Saldo total do FIS: R$%.2f." %soma1

media1 = soma1 / cont1

print "Média das contribuições: R$%.2f." %media1
