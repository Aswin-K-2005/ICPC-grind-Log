import sys
input = sys.stdin.readline

def solve():
    w = int(input())
    if w>2:
        if w % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
