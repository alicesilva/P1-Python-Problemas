# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# mdc por euclides

m = int(raw_input())
n = int(raw_input())

maior = m
menor = n

if n > maior:
	maior = n
else:
	maior = m
if m < menor:
	menor = m
else:
	menor = n
while menor != 0:
	resto = maior % menor
	maior = menor
	menor = resto
	
print maior
