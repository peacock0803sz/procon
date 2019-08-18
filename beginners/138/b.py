n = int(input())
resistors = [int(i) for i in input().split()]
reverse = []
for i in range(len(resistors)):
    reverse.append(1 / resistors[i])
print(1 / sum(reverse))
