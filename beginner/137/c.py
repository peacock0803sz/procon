from collections import Counter

n = int(input())
s = [input() for i in range(n)]
st = []
ans = 0
for i in range(n):
    st.append(list(tuple(s[i])))
    st[i].sort()
    st[i] = str(st[i])
st.sort()
count = Counter(st).values()
print(st)
print(count)
print(ans)
