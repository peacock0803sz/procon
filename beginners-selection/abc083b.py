n, a, b = map(int, input().split())
answer = 0
for i in range(1, n + 1):
    if a <= sum(list(map(int, list(str(i))))) <= b:
        answer += i
print(answer)
