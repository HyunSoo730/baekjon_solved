
# 수영장. 1년동안 각 달의 이용 계획 수립, 가장 적은 비용으로 수영장 이용할 수 있는 방법 찾기
# 이용권 4종류 : 1일권, 1달권, 3달권, 1년권

# 1년치 이용계획이 주어질 때, 가장 적은 비용으로 수영장 이용할 수 있는 방법 찾기.

def DFS(L, sum_value):
    global res
    # print(f"{L+1}번달 까지의 상황 : {sum_value}")
    if L >=12: # 모든 달 확인
        res = min(res, sum_value)
    else: # 현재 달을 어떻게 할 것인지
        if plan[L] > 0:
            DFS(L+1, sum_value + plan[L] * 이용권[0]) # 1일권으로 이번달 해결
            DFS(L+1, sum_value + 이용권[1]) # 한달권으로 해겷
            DFS(L+3, sum_value + 이용권[2]) # 3달권으로 해결
        else: # 그냥 넘어가
            DFS(L+1, sum_value)

T = int(input())
for t in range(1,T+1):
    이용권 = list(map(int, input().split())) # 1일, 한달, 3달, 일년 이용권 정보
    plan = list(map(int, input().split())) # 1월~12월까지 이용계획
    res = 이용권[3] # 1년치를 최소값으로 보고 진행
    DFS(0,0)
    print(f"#{t} {res}")