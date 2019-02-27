n, a, b = int(input())


def digits_sum(x):
    sum = 0
    if x > 0:
        sum += x % 10
        x /= 10
    return sum


answer = 0
for i in (n + 1):
    if a < digits_sum(n) < b:
        answer += 1
print(answer)
