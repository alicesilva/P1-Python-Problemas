#coding: utf-8
#Aluna: Alice Fernandes Silva / Programação 1, 2015
#questão: zera não-nulos

def zera_nao_nulos(m,lin,col):
	for i in range(len(m)):
		if i == lin:
			for j in range(len(m[i])):
				if j == col:
					if m[i][j] == 1:
						for k in range(j-1,-1,-1):
							if m[i][k] == 1:
								m[i][k] = 0
							else:
								break
						for k in range(j,len(m[i])):
							if m[i][k] == 1:
								m[i][k] = 0
							else:
								break
						for k in range(i-1,-1,-1):
							if m[k][j] == 1:
								m[k][j] = 0
							else:
								break
						for k in range(i+1,len(m)):
							if m[k][j] == 1:
								m[k][j] = 0
							else:
								break
