#coding: utf-8
def valorPagamento():
	cont = 0
	valores = []
	while True:
		prestacao = float(raw_input())
		if prestacao == 0:
			break
		dias = int(raw_input())
		cont += 1
		if dias == 0:
			valor = prestacao
			valores.append(valor)
		if dias != 0:
			multa = (prestacao * 3/ 100.0)
			juros_dia = (0.1 / 100.0 * dias) * prestacao
			valor = prestacao + multa + juros_dia
			valores.append(valor)
		
		print valor
	soma = 0
	for i in range(len(valores)):
		soma += valores[i]
	
	print soma
	print cont

if __name__ == "__main__":
	valorPagamento()
