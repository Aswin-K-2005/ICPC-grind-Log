import sys
input = sys.stdin.readline

def solve():
    m, n = map(int, input().split())
    print((m * n) // 2)

if __name__ == "__main__":
    solve()
