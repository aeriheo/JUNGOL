s, e = map(int, input().split())
# s와 e는 2<=s, e<=9
while s<2 or s>9 or e<2 or e>9:
    print("INPUT ERROR!")
    # 다시 입력받기
    s, e = map(int, input().split())

# s ~ e까지의 범위
result = {}

if s>e:
    for i in range(s, e-1, -1):
        result[i] = []
else:
    for i in range(s, e+1):
        result[i] = []


# 곱셈값 저장
for i in range(1, 10):
    for idx in result.keys():
        result[idx].append(idx*i)

# 출력
for i in range(9):
    for idx in result.keys():
        print(idx, "*", i+1, "=", end='')
        # 9 * 9가 최대 100미만이므로 최대 길이는 두 자리수
        # 한 자리 수일 때는 공백을 하나 추가
        if result[idx][i]<10:
            print(" ", result[idx][i], end='   ')
        else:
            print("", result[idx][i], end='   ')
    print()