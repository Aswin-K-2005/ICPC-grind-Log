import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    count = 0
    for _ in range(t):
        a, b, c = map(int, input().split())
        if a + b + c >= 2:
            count += 1
    print(count)

if __name__ == "__main__":
    solve()
