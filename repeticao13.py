#coding: utf-8
base = int(raw_input())
expoente = int(raw_input())

exponeciacao = 1

for i in range(expoente):
	exponeciacao *= base

print exponeciacao
