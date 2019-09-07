stdin = [int(x) for x in input().split()]
entry = 1
adptr = 0
while entry < stdin[1]:
    entry -= 1
    entry += stdin[0]
    adptr += 1
print(adptr)
