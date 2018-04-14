# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Quantidade de inteiros divisivéis por K
contador = 0
K = int(raw_input())
n = int(raw_input())

for i in range(n):
	numero  = int(raw_input())
	if numero % K == 0:
		contador += 1

percentual = float(contador) / n * 100
		
print "%d (%.1f%%)" %(contador,percentual)
