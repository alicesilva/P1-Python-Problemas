# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015
# Espaço em disco

def conversao_bytes(valores):
	megas_bytes = []
	for i in range(len(valores)):
		mega = float(valores[i]) / 1048576.0
		megas_bytes.append(mega)
	return megas_bytes


def percentual(megas_bytes,total):
	percentuais = []
	for i in range(len(megas_bytes)):
		percentual = (megas_bytes[i]/total) * 100
		percentuais.append(percentual)
	return percentuais

nomes = []
valores = []
while True:
	dados = raw_input()
	if dados == "fim":
		break
	lista = dados.split()
	nome = lista[0]
	nomes.append(nome)
	valor = lista[1]
	valores.append(valor)
	
mega_bytes = conversao_bytes(valores)
total = 0
for i in range(len(mega_bytes)):
	total += mega_bytes[i]

percentuais = percentual(mega_bytes,total)

print "SPLab - Espaço utilizado pelos usuários"
print "---------------------------------------------"
print "Nr., Usuário, Espaço Utilizado, % do uso"
print 
for i in range(len(mega_bytes)):
	print "%d, %s, %.2f MB, %.2f%%" %(i+1,nomes[i],mega_bytes[i],percentuais[i])
print
print "Espaço total ocupado: %.2f MB" %total
print "Espaço médio ocupado: %.2f MB" %(total/len(mega_bytes))	
	
	
