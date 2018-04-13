#coding: utf-8
def get_items(valores, indices):
	novos_valores = []
	for item in indices:
		if item > len(valores) or item < 0:
			novos_valores.append(None)
		else:
			novos_valores.append(valores[item])
			
	return novos_valores

valores = [18, 22, 73, 32, 19, 21, 43]
indices = [3, 4, 8, 1]
assert get_items(valores, indices) == [32, 19, None, 22]
		
