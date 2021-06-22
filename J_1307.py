from collections import deque
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arr = deque(arr)

n = int(input())
answer = [[] for _ in range(n)]
for _ in range(n):
    for i in range(n-1, -1, -1):
        data = arr.popleft()
        answer[i].insert(0, data)
        arr.append(data)

for lst in answer:
    for data in lst:
        print(data, end = ' ')
    print()
