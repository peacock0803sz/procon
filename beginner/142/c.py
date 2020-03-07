import sys


def main():
    n = int(input())
    a = [int(i) for i in sys.stdin.readline().split()]
    ans = [0] * n
    for i in range(n):
        ans[a[i] - 1] = i + 1
    print(*ans)


if __name__ == "__main__":
    main()
