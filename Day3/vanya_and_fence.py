import sys
input = sys.stdin.readline

def solve():
    n, h = map(int, input().split())
    friends = list(map(int, input().split()))
    count = sum(1  if height <= h else 2 for height in friends )  
    print(count)

if __name__ == "__main__":
    solve()
