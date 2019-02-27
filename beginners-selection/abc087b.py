a = int(input())
b = int(input())
c = int(input())
x = int(input())

answer = 0
for i in (a + 1):
    for j in (b + 1):
        for k in (c + 1):
            if i * 500 + j * 100 + k * 50 == x:
                answer += 1
print(answer)
