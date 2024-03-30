import sys

n,L = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

res = 0
# ! 먼저 행 먼저 판단
for i in range(n):
    count = 1
    for j in range(n-1):
        if abs(g[i][j] - g[i][j+1]) > 1: break # 높이 차가 1보다 크면 안된다.

        if g[i][j] == g[i][j+1]: # 다음 좌표랑 동일하면
            count += 1
        elif g[i][j] + 1 == g[i][j+1]: # 오름
            if count >= L: # 가능한 경우
                count = 1 # 다시 1로 초기화
            else:
                break
        elif g[i][j] == g[i][j+1]+1: # 내림인 경우
            if count < 0: break
            count = -(L-1)
    else: # 반복문을 다 돌았다는 건 가능한 경우가 될 수 있따.
        if count >= 0:
            # print(f"{i}번쨰 행은 추가 가능")
            res += 1

# 열에 대해서도 똑같이 판단
for j in range(n):
    count = 1
    for i in range(n-1):
        if abs(g[i][j] - g[i+1][j]) > 1: break
        if g[i][j] == g[i+1][j]: # 같은 경우는 +1
            count += 1
        elif g[i][j] + 1 == g[i+1][j]: # 오름
            if count >= L: # 가능한 경우
                count = 1
            else:
                break
        elif g[i][j] == g[i+1][j] + 1: # 내림
            if count < 0: break
            count = -(L-1)
    else: # 반복문 다 돈 것은 가능한 경우가 될 수 있음
        if count >= 0:
            # print(f"{j}번째 열은 추가 가능")
            res += 1
print(res)