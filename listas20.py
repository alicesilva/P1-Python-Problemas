#coding: utf-8
print "Projeção de Gastos com Abono"
print "============================"
print 

salarios = []
abonos = []
cont = 0

while True:
	salario = float(raw_input("Salário: "))
	if salario == 0:
		break
	cont += 1
	abono = 20 / 100.0 * salario
	if abono < 100.0:
		abono = 100
	salarios.append(salario)
	abonos.append(abono)

print
print "Salário    - Abono "

for i in range(len(salarios)):     
	print "R$ %.2f - R$ %.2f" %(salarios[i],abonos[i])

print
print "Foram processados %d colaboradores" %cont

soma = 0
cont_menor = 0
maior = abonos[0]

for i in range(len(abonos)):
	soma += abonos[i]
	if abonos[i] == 100:
		cont_menor += 1
	if abonos[i] > maior:
		maior = abonos[i]

print "Total gasto com abonos: R$ %.2f" %soma
print "Valor mínimo pago a %d colaboradores" %cont_menor
print "Maior valor de abono pago: R$ %.2f" %maior
	

