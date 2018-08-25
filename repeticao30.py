#coding: utf-8
preco = float(raw_input())

print "Preço do pão: R$ %.2f" %preco

for i in range(1,51):
	print "%d- R$ %.2f" %(i,i*preco)
	
