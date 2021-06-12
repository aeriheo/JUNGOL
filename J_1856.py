n, m = map(int, input().split())
data = [[] for _ in range(n)]
num = 1
for i in range(1, n+1):
    for _ in range(m):
        if i%2==1:
            data[i-1].append(num)
        else:
            data[i-1].insert(0, num)
        num += 1

for i in range(n):
    for data_num in data[i]:
        print(data_num, end = ' ')
    print()