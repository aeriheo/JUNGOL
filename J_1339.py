from collections import deque
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
arr = deque(arr)

n = int(input())
answer = [[] for _ in range(n)]
if 1>n or n>100 or n%2==0:
    print("INPUT ERROR")
else:
    mid = n//2
    start = mid
    end = mid
    for _ in range((n+1)//2):
        for i in range(start, end+1):
            data = arr.popleft()
            answer[i].insert(0, data)
            arr.append(data)
        start -= 1
        end += 1
    for lst in answer:
        for data in lst:
            print(data, end = ' ')
        print()
