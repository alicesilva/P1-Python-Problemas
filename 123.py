#coding: utf-8

def tem123plus(l):
	indice = -1
	for i in range(len(l)):
		if l[i] == 1:
			for j in range(i,len(l)):
				if l[j] == 2:
					for k in range(j,len(l)):
						if l[k] == 3:
							for m in range(len(l)):
								if l[m] == 1:
									indice = m
									break
	
	return indice


assert tem123plus([3,2,1,2,3]) == 2
assert tem123plus([4,1,1,1,4,2,3]) == 1
assert tem123plus([1,2,2,3]) == 0
assert tem123plus([1,2,2,4]) == -1
