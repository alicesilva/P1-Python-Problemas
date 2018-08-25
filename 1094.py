#coding: utf-8
N = int(raw_input())

lista_quantia = []
lista_tipo = []
soma = 0
coelhos = 0
ratos = 0
sapos = 0

for i in range(N):
	testes = raw_input()
	dados = testes.split()
	quantia = int(dados[0])
	tipo = dados[1]
	lista_quantia.append(quantia)
	lista_tipo.append(tipo)

for quantidade in lista_quantia:
	soma += quantidade
	
print "Total: %d cobaias" %soma

for item in range(len(lista_tipo)):
	if lista_tipo[item] == "C":
		coelhos += lista_quantia[item]
	if lista_tipo[item] == "R":
		ratos += lista_quantia[item]
	if lista_tipo[item] == "S":
		sapos += lista_quantia[item]
		
print "Total de coelhos: %d" %coelhos
print "Total de ratos: %d" %ratos
print "Total de sapos: %d" %sapos

percentual_coelhos = coelhos / float(soma) * 100.0
percentual_ratos = ratos / float(soma) * 100.0
percentual_sapos = sapos / float(soma) * 100.0

print "Percentual de coelhos: %.2f %%" %percentual_coelhos
print "Percentual de ratos: %.2f %%" %percentual_ratos
print "Percentual de sapos: %.2f %%" %percentual_sapos
