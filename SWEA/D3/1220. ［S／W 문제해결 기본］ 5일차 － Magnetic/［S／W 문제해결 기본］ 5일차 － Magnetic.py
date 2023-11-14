
# 1은 N극 2는 S극
# 빨강(1)은 아래로, 파랑은 위로 가려고 함.
T = 10
for t in range(1,T+1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    stack = []
    cnt = 0
    for i in range(n):
        isRed = False
        for j in range(n):
            if data[j][i] == 1:
                isRed = True
            if data[j][i] == 2 and isRed == True:
                cnt += 1
                isRed = False
    print(f"#{t} {cnt}")
