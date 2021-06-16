def typeOne(n):
    for i in range(1, n+1):
        for _ in range(n):
            print(i, end = ' ')
        print()

def typeTwo(n):
    for i in range(n):
        if i%2==0:
            for num in range(1, n+1):
                print(num, end = ' ')
        else:
            for num in range(n, 0, -1):
                print(num, end = ' ')
        print()

def typeThree(arr, n):
    num = 1
    start = 1
    for _ in range(n):
        num = start
        for i in range(n):
            arr[i].append(num)
            num += start
        start += 1

    for idx in arr:
        for data in idx:
            print(data, end = ' ')
        print()

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
if m == 1:
    typeOne(n)
elif m == 2:
    typeTwo(n)
elif m == 3:
    typeThree(arr, n)