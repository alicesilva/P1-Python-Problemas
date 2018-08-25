#coding: utf-8
produto1 = float(raw_input("Qual o preço do produto 1? "))
produto2 = float(raw_input("Qual o preço do produto 2? "))
produto3 = float(raw_input("Qual o preço do produto 3? "))

barato = produto1

if barato > produto2 and produto2 < produto3:
	print "Deve comprar o produto 2."
elif barato > produto3 and produto3 < produto2:
	print "Deve comprar o produto 3."
else:
	print "Deve comprar o produto 1."
	
