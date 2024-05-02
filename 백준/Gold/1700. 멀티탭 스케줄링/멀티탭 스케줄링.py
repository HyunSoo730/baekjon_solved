import sys
from collections import deque


n,k = map(int, input().split())
data = list(map(int, input().split())) # k개의 각 전기용품 어떤 거 썼는지

# 핵심은 만약 이미 최대치로 꽂혀있다면 가장 나중에 사용될 제품을 뽑아야 한다. (그래야 중복 최소화)

def 가장늦게사용하는제품뽑기():
    if not dq:
        return
    last_idx = -1 #  가장 마지막으로 사용될 때의 인덱스
    last_num = -1 # 가장 마지막으로 사용하는 제품의 번호
    for num in check: # 현재 멀티탭에 꽂혀있는 애들 꺼내서
        if num not in dq: # 남은 것들중에 존재하지 않음. -> 이놈을 뽑아야함
            last_num = num # 갱신 후 바로 끝.
            break
        else: # 현재 존재한다면 인덱스 갱신
            idx = dq.index(num)
            if idx > last_idx:
                last_idx = idx
                last_num = num
    check.remove(last_num)


dq = deque(data)
check = set()
res = 0
while dq: # 아직 존재한다면
    now = dq.popleft() # 현재 콘센트
    if now in check: # 이미 존재하면 필요없음
        continue
    if len(check) < n: # 여유공간 존재
        check.add(now)
    else: # 여유공간 없다면 가장 마지막에 사용되는 것 뽑아야 함.
        가장늦게사용하는제품뽑기()
        res += 1 # 횟수 추가
        check.add(now) # 지웠으니 현재꺼 추가.
print(res)