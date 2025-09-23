import sys

# N일동안 M번만 통장에서 돈 뺌
# 통장에서 k원 인출, k원으로 하루를 보낼 수 있으면 그대로 사용
# 모자라면 남은 금액은 통장에 집어넣고 다시 k원 인출
# 인출금액 k를 최소화, 필요한 최소 금액 k
# M번을 맞추기 위해 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 넣고, 다시 K원 인출 가능
# 즉 M번 이하면 그냥 가능하다고 본다 ?

n,m = map(int, input().split())
data = []
for _ in range(n):
    cost = int(input())
    data.append(cost) # i번째 날에 이용할 금액이 주어짐.
# 최적화 : k의 최소값
# 결정 : k원으로 했을 때 M번 이하 인출로 모두 처리 가능한가 ?

def is_possible(cost): # 해당 비용으로 M번 이하 인출로 가능해 ? -> k원으로 가능한가의 k원은 결국 가장 큰 값이어야 함.
    # 즉, 하루 최대 사용액 이상이어야 함 !
    # 또한 right도 전체 합이어야 함 ->
    cnt = 1 # 인출 횟수 (시작 1)
    now_cost = cost # 시작
    for i in range(n):
        if now_cost >= data[i]: # 가능
            now_cost -= data[i]
        else: # 불가능
            now_cost = cost - data[i]
            cnt += 1
    return cnt <= m

left, right = max(data), sum(data) + 1
# 극단적으로 M이 1인 경우. -> 모든 날 처리 혹은.. 제시된 범위에서 10000이 금액의 최대라고 되어 있음.
# 어쨋든 K는 최소 sum(data)여야 함. 인출 1번만 허용할 경우 대비 !
while left < right:
    mid = (left + right) // 2 # k원으로 가능한가 ?

    if not is_possible(mid): # 불가능
        left = mid + 1  # 불가능하면 최소 금액 늘려야지
    else:
        right = mid

print(left)