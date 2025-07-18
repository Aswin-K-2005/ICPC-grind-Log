import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    for _ in range(n):
        word = input().strip()
        if len(word) > 10:
            print(word[0] + str(len(word) - 2) + word[-1])
        else:
            print(word)

if __name__ == "__main__":
    solve()
