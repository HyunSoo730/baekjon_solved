
# 가장 적은 비용으로 수영장을 이용할 수 있는 방법
# 수영장 이용권 4종료

# 각 이용권의 요금과 각 달의 이용 계획이 주어질 때 가장 적은 비용으로 수영장을 이용할 수 있는 방법
# -> DFS

def DFS(L, money): # 현재 확인하고 있는 달, 현재까지 돈, 한달 이용권인지, 석달 이용권인지, 1년 이용권인지
    global res
    if L >= 12:
        res = min(res, money)
    else:
        if plan[L] > 0: # 처리해야 하는 경우
            DFS(L+1, money + data[0] * plan[L]) # 1일권으로 현재 월을 처리
            DFS(L+1, money + data[1]) # 1달권으로 현재 월을 처리
            DFS(L+3, money + data[2]) # 3달권으로 처리
        else: # 처리하지 않아도 되면 그냥 넘어가
            DFS(L+1, money)

T = int(input())
for t in range(1,T+1):
    data = list(map(int, input().split())) # 이용권 가격 1일, 1달, 3달, 1년
    plan = list(map(int, input().split())) # 12개월 이용계획
    MAX = data[-1] # 1년 이용권을 썼을 때를 최대로 두고 계산

    res = MAX # 1년권을 일단 최소 금액이라고 생각하고 진행
    DFS(0,0)
    print(f"#{t} {res}")
