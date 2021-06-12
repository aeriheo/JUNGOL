n, m = map(int, input().split())
num = 1
for _ in range(n):
    for __ in range(m):
        print(num, end = ' ')
        num += 1
    print()