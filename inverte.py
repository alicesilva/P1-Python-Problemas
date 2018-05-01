# coding: utf-8
# Aluna: Alice Fernandes Silva /UFCG, 2015.1, Programação 1
# Altera consecutivos

def inverte2a2(seq):
	if len(seq) % 2 == 0:
		cont_um = 0
		cont_mais_um = 1
		for i in range(len(seq)):
			if cont_mais_um <= len(seq) -1 and cont_um <= len(seq):
				seq[cont_um], seq[cont_mais_um] = seq[cont_mais_um], seq[cont_um]
				cont_um += 2
				cont_mais_um += 2
	else:
		cont_um = 0
		cont_mais_um = 1
		for i in range(len(seq)-1):
			if cont_mais_um <= len(seq)-2 and cont_um <= len(seq)-1:
				seq[cont_um], seq[cont_mais_um] = seq[cont_mais_um], seq[cont_um]
				cont_um += 2
				cont_mais_um += 2
	
	return seq
