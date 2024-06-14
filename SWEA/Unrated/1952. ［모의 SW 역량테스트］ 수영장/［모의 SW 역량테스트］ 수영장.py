
# 수영장 이용. 가장 적은 비용 사용하기
# 4가지 경우 존재.

def DFS(L, now):
    global res
    if L >= 12: # 모든 달 확인
        res = min(res, now)
    else:
        if 계획[L] > 0: # 현재 달이 존재하는 경우
            DFS(L+1, now + 이용권[0] * 계획[L])
            DFS(L+1, now + 이용권[1])
            DFS(L+3, now + 이용권[2])
        else:
            DFS(L+1, now)

T = int(input())
for t in range(1,T+1):
    이용권 = list(map(int, input().split()))
    계획 = list(map(int, input().split())) # 각 달의 계획

    res = 이용권[-1] # 1년치의 경우를 최소값으로 생각하고 진행
    DFS(0,0)
    print(f"#{t} {res}")