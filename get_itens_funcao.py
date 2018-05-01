# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Get itens

def get_items(valores,indices):
	novos_valores = []
	novos_indices = []
	for i in range(len(indices)):
		for item in range(len(valores)):
			novos_indices.append(item)
			if indices[i] == item:
				novos_valores.append(valores[item])
		if indices[i] not in novos_indices:
			novos_valores.append(None)
	return novos_valores

valores = [18, 22, 73, 32, 19, 21, 43]
indices = [3, 4, 8, 1]
assert get_items(valores, indices) == [32, 19, None, 22]

valores = []
indices = [2,3]
assert get_items(valores, indices) == [None, None]

valores = [2,3]
indices = []
assert get_items(valores, indices) == []


