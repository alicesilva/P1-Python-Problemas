#coding: utf-8
def inverte2a2_condicional(seq):
	if len(seq) % 2 == 0:
		for i in range(len(seq)):
			if i % 2 == 0:
				if seq[i] > seq[i+1]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
	if len(seq) % 2 != 0:
		for i in range(len(seq)-1):
			if i % 2 == 0:
				if seq[i] > seq[i+1]:
					seq[i], seq[i+1] = seq[i+1], seq[i]
	return
