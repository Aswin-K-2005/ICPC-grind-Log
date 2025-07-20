import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    n = int(input())
    games = input().strip()
    frequencies = Counter(games)
    if frequencies['A'] > frequencies['D']:
        print("Anton")
    elif frequencies['A'] < frequencies['D']:
        print("Danik")
    else:
        print("Friendship")

if __name__ == "__main__":
    solve()
