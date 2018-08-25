#coding: utf-8
temperaturas = []
soma = 0

for i in range(12):
	temperatura = float(raw_input())
	temperaturas.append(temperatura)
	soma += temperatura
	

media = soma / 12

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

for i in range(len(temperaturas)):
	if temperaturas[i] > media:
		print "%.1f, %d - %s" %(temperaturas[i],i+1,meses[i])
		
