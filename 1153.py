#coding: utf-8
N = int(raw_input())

multiplicacao = 1

for i in range(1,N):
    multiplicacao *= (N-i)

fatorial = multiplicacao * N

print fatorial
