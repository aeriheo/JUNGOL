from collections import deque
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arr = deque(arr)

n = int(input())
answer = [[] for _ in range(n)]
for i in range(n):
    data = arr.popleft()
    answer[i].append(data)
    arr.append(data)
    for j in range(i+1, n):
        data = arr.popleft()
        answer[j].append(data)
        arr.append(data)

for lst in answer:
    blank = n - len(lst)
    for i in range(blank):
        print(' ', end = ' ')
    for data in lst:
        print(data, end = ' ')
    print()