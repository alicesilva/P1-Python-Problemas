# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Operações inválidas

limite_saques = int(raw_input())
saldo = float(raw_input())
cont = 0

while True:
	entrada = raw_input()
	dados = entrada.split()
	operacao = dados[0]
	valor = float(dados[1])
	if operacao == "saque":
		cont += 1
	if operacao == "depósito" and valor > 1000 or cont > limite_saques:
		break
	if operacao == "saque":
		saldo -= valor
	else:
		saldo += valor
	if saldo < 0:
		break


print "Operação inválida: %s." %entrada
print "Seu saldo é R$ %.2f." %saldo
