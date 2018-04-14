# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Consoantes
n = int(raw_input())
contador = 0
for i in range(n):
	palavra = raw_input()
	if palavra[0] in "bcdfghjklmnpqrstVwyzxBCDFGHJKLMNPQRSTVWYXZ":
		contador += 1

percentual = float(contador) / n * 100.0

print "total de palavras: %d" %n 
print "iniciadas por consoantes: %d (%.2f%%)" %(contador,percentual)
