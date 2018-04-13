# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Serie: substituindo terminados em 7 ou divisíveis por 7
for i in range(1,102,2):
	if i % 7 == 0 or str(i)[-1] == "7":
		print "*"
	else: 
		print i 
