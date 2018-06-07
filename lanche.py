# coding: utf-8
# Aluna: Alice Fernandes Silva /Programação 1, 2015.1
# Lanche mais pedido

def lanchemaispedido(pedidos):
	auxiliar = []
	for i in range(len(pedidos)):
		if pedidos[i] not in auxiliar:
			auxiliar.append(pedidos[i])
	contadores = []
	for i in range(len(auxiliar)):
		cont = 0
		for j in range(len(pedidos)):
			if auxiliar[i] == pedidos[j]:
				cont += 1
		contadores.append(cont)
	
	for i in range(len(contadores)):
		if contadores[i] > len(pedidos) / 2:
			return auxiliar[i]
