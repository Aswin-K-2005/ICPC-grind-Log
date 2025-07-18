import sys
input = sys.stdin.readline

def solve():
    n, s = map(int, input().split())
    positions = list(map(int, input().split()))
    count=0
    for i in range(n):
        if positions[i] >= s:
             pos=i
             break
    for pos in range(n):
     count += s- positions[i] 
     s= positions[i]
    while pos >=0:
        count += s- positions[pos] 
        s= positions[pos]
        pos -= 1
 
    return print(count)

t = int(input())
for _ in range(t):
    solve()
