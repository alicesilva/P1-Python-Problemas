#coding: utf-8
def inverte2a2(seq):
	if len(seq) % 2 == 0:
		for i in range(len(seq)):
			if i % 2 == 0:
				seq[i] , seq[i+1] = seq[i+1] , seq[i]
	else:
		for i in range(len(seq)-1):
			if i % 2 == 0:
				seq[i] , seq[i+1] = seq[i+1] , seq[i]
	return
