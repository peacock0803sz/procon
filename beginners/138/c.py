import math
import itertools

n = int(input())
v = [int(i) for i in input().split()]
ans = []
comb = list(itertools.combinations(v, 2))
for i in range(len(comb)):
    list(comb[i])
    ans.append((comb[i][0] + comb[i][1]) / 2)
    print((comb[i][0] + comb[i][1]) / 2)
print(max(ans))
