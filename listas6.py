#coding: utf-8
medias = []
i = 0

for i in range(10):
	i += 1
	print "Aluno %d:" %i
	soma = 0
	for i in range(4):
		nota = float(raw_input())
		soma += nota
	media = soma / 4
	medias.append(media)

print

j = 1
cont = 0

for i in range(len(medias)):
	print "Aluno %d: %.2f" %(j,medias[i])
	j += 1
	if medias[i] >= 7.0:
		cont += 1

print
print cont
