# coding: utf-8
# Aluna:Alice Fernandes Silva/UFCG, 2015.1, Programação 1
# Op bancarias

nome_saldo = raw_input()

entrada = nome_saldo.split()
nome = entrada[0]
saldo_inicial= float(entrada[1])

while True:
	codigo = raw_input()
	if codigo == "3":
		break
	entrada1 = codigo.split()
	if entrada1[0] == "1":
		saldo_inicial -= float(entrada1[1])	
	if entrada1[0] == "2":
		saldo_inicial += float(entrada1[1])

print "Saldo de R$ %.2f na conta de %s" %(saldo_inicial,nome)

