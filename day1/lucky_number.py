import sys
input = sys.stdin.readline

def solve():
    n = input().strip()
    count = sum(1 for digit in n if digit in ('4', '7'))
    if count in (4, 7):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
