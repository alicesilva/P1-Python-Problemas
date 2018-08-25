#coding: utf-8
vetor = [3,5,6,7,8,9,10]
soma = 0
multiplicacao = 1

for i in range(len(vetor)):
	soma += vetor[i]
	multiplicacao *= vetor[i]
	print vetor[i]

print soma
print multiplicacao
