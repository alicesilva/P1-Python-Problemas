#coding: utf-8
def selection_sort(l):
	for i in range(len(l)):
		index_min = i
		for j in range(i+1,len(l)):
			if l[index_min] > l[j]:
				index_min = j
		l[index_min] , l[i] = l[i] , l[index_min]
	
	return l

l = [1,5,6,7,8,9,2,3]
print selection_sort(l)
