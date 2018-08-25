#coding: utf-8
print "Comparativo de Consumo de Combustível"
print

i = 0
nomes = []
mil_km = []
quilometros = []

for i in range(5):
	i += 1
	print "Veículo %d" %i	
	nome = raw_input("Nome: ")
	quantidade = float(raw_input("Km por litro: "))
	mil_quil = 1000.0 / quantidade
	nomes.append(nome)
	quilometros.append(quantidade)
	mil_km.append(mil_quil)

custos = []

for i in range(len(mil_km)):
	custo = mil_km[i] * 2.25
	custos.append(custo)

print
print "Relatório Final"

j = 0
for i in range(len(nomes)):
	j += 1
	print "%d - %s           -    %.1f -  %.1f litros - R$ %.2f" %(j,nomes[i],quilometros[i],mil_km[i],custos[i])
	
menor = custos[0]
for i in range(len(custos)):
	if custos[i] < menor:
		menor = custos[i]
		carro = nomes[i]

print "O menor consumo é do %s." %carro
