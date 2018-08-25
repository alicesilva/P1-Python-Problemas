#coding: utf-8
nota1 = float(raw_input())
nota2 = float(raw_input())

media = (nota1 + nota2) / 2.0

print nota1
print nota2
print media

if 9.0 < media <= 10.0:
	conceito = "A"
if 7.5 < media <= 9.0:
	conceito = "B"
if 6.0 < media <= 7.5:
	conceito = "C"
if 4.0 < media <= 6.0:
	conceito = "D"
if media <= 4.0:
	conceito = "E"

print conceito

if conceito == "A" or conceito == "B" or conceito == "C":
	print "Aprovado"
else:
	print "Reprovado"
