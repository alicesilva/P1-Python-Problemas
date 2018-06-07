#coding: utf-8
def inserction_sort(l):
	for i in range(1,len(l)):
		for j in range(1,len(l)):
			if l[j] < l[j-1]:
				l[j-1], l[j] = l[j], l[j-1]
	return l

l = [1,5,6,4,7,8,9,2,3]
print inserction_sort(l)
