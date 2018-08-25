#coding: utf-8
n = int(raw_input())

soma = 0

for i in range(n):
	idades = int(raw_input())
	soma += idades

media = soma / n

if 0 <= media <= 25:
	print "Jovem"
elif 26 <= media <= 60:
	print "Adulta"
elif media > 60:
	print "Idosa" 
