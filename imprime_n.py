#coding: utf-8
def imprime():
	n = int(raw_input())
	for i in range(n):
		i += 1
		for j in range(i):
			print i,
		print

if __name__ == "__main__":
	imprime()
