import sys


def main():
    n = int(input())
    a = [int(i) for i in sys.stdin.readline().split()]
    ans = []
    ans_append = ans.append
    for i in range(n):
        ans_append(a.index(i + 1) + 1)
    print(*ans)


if __name__ == "__main__":
    main()
