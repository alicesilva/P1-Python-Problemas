#codig: utf-8

vetores = []

for i in range(10):
	vetor = int(raw_input())
	if vetor <= 0:
		vetor = 1
	vetores.append(vetor)

for i in range(len(vetores)):
	print "X[%d] = %d" %(i,vetores[i])
