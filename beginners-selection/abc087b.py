a = 500 * int(input())
b = 100 * int(input())
c = 50 * int(input())
x = int(input())

if x < a + b + c:
    print(0)
elif x == a + b + c:
    print(1)
elif x % a == 0 and b == 0 and c == 0:
    print(1)
elif a == 0 and x % b == 0 and c == 0:
    print(1)
elif a == 0 and b == 0 and x % c == 0:
    print(1)
