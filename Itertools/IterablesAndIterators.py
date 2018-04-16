from itertools import combinations

N,L,K = int(input()), input().split(), int(input())
C = list(combinations(L, K))
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F))/len(C)))
