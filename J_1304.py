n = int(input())
arr = [[] for _ in range(n)]
num = 1
for _ in range(n):
    for i in range(n):
        arr[i].append(num)
        num += 1

for idx in arr:
    for data in idx:
        print(data, end = ' ')
    print()