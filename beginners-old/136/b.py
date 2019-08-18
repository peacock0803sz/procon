n = int(input())
odd = []
for i in range(1, n + 1):
    if len(str(i)) % 2 == 1:
        odd.append(i)
print(len(odd))
