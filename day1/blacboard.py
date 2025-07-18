def main():
    
        n = int(input())
        count = [0, 0, 0, 0]
        for i in range(n):
            count[i % 4] += 1
        if count[0] == count[3] or count[1] == count[2]:
            print("Alice")
        else:
            print("Bob")

for i in range (5):
    main()
