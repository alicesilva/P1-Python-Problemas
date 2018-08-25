#coding: utf-8
cont_alcool =0
cont_gasolina =0
cont_diesel = 0

while True:
	n = int(raw_input())
	if n == 4:
		break
	if n == 1:
		cont_alcool += 1
	if n == 2:
		cont_gasolina += 1 
	if n == 3:
		cont_diesel += 1

print "MUITO OBRIGADO"
print "Alcool: %d" %cont_alcool
print "Gasolina: %d" %cont_gasolina
print "Diesel: %d" %cont_diesel
