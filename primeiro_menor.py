# coding: utf-8
# Aluna: Alice Fernandes Silva / Programação 1, 2015.1
# Primeiro menor

def primeiro_menor(num, numeros):
	cont = 0
	for i in range(len(numeros)):
		if int(numeros[i]) < num:
			return i
			break
		if int(numeros[i]) >= num:
			cont += 1
	if cont == len(numeros):
		return -1


def main():
	numeros = raw_input()
	num = int(raw_input())
	lista_numeros = numeros.split()
	cont = 0
	for i in range(len(lista_numeros)):
		if int(lista_numeros[i]) < num:
			print "primeiro menor que %d: %d" %(num, int(lista_numeros[i]))
			break
		if int(lista_numeros[i]) >= num:
			cont += 1
	if cont == len(lista_numeros):
		print "sem menores que %d" %num
		
	primeiro_menor(num, lista_numeros)

if __name__ == '__main__':
    main()
	
	
