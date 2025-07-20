import sys
input = sys.stdin.readline

def solve():
    a = input().strip().lower()
    b = input().strip().lower()
    if a<b:
        print(-1)

    elif a>b:
        print(1)
    else:
        print(0)    
   

if __name__ == "__main__":
    solve()
