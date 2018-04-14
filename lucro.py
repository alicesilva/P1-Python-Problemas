# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Lucro mensal uma empresa
lista = []
for i in range(12):
	entrada = raw_input()
	entrada1 = entrada.split()
	receita = float(entrada1[0])
	despesa = float(entrada1[1])
	diferenca = receita - despesa
	lista.append(diferenca)

print "jan %4.1f" %(lista[0])
print "fev %4.1f" %(lista[1])
print "mar %4.1f" %(lista[2])
print "abr %4.1f" %(lista[3])
print "mai %4.1f" %(lista[4])
print "jun %4.1f" %(lista[5])
print "jul %4.1f" %(lista[6])
print "ago %4.1f" %(lista[7])
print "set %4.1f" %(lista[8])
print "out %4.1f" %(lista[9])
print "nov %4.1f" %(lista[10])
print "dez %4.1f" %(lista[11])
	
	
