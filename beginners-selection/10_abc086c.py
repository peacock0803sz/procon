n = int(input())
for i in range(n):
    t, x, y = 0, 0, 0
    t_dash, x_dash, y_dash = map(int, input().split())
    duration = t_dash - t
    dist = abs(x_dash - x) + abs(y_dash - y)
    if dist > duration or (duration - dist) % 2 != 0:
        print('No')
        exit(0)
    t, x, y = t_dash, x_dash, y_dash
print('Yes')
