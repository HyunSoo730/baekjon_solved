import sys
# n개의 건물
# 현재 있는 건물 기준 현재 있는 건물의 높이 L보다 큰 곳의 건물만 볼 수 있다.
# N^2으로 풀 수 없음
# 만약 볼 수 있는 건물의 개수 1개 이상 -> 거리가 가장 가까운 거리에 있는 번호
n = int(input())
data = list(map(int, input().split())) # 각 건물 높이
cnt = [0] * n
INF = int(1e9)
dis = [(INF, INF)] * n

# 먼저 왼쪽에서부터 시작
# 왼쪽에서 오른쪽으로 순회할 때 : 거리 = 현재 위치 - 스택의 top 인덱스 : i - stack[-1]
stack = []
for i in range(n):
    now = data[i] # 현재 값
    while stack and data[stack[-1]] <= now:
        stack.pop()
    cnt[i] += len(stack)
    if stack:
        dis[i] = (i - stack[-1], stack[-1]) # (거리, 인덱스 번호)
    stack.append(i)

# 오른쪽에서부터 시작
# 오른쪽에서 왼쪽으로 순회할 때 : 거리 = 스택의 top 인덱스 - 현재 위치 = stack[-1] - i
stack = []
now_cnt = 0
for i in range(n-1, -1, -1):
    now = data[i]
    while stack and data[stack[-1]] <= now:
        stack.pop()
    cnt[i] += len(stack)
    # 거리가 더 가깝거나, 거리가 같을 때 번호가 더 작은.
    if stack:
        now_dis = stack[-1] - i
        if now_dis < dis[i][0] or (now_dis == dis[i][0] and stack[-1] < dis[i][1]):
            dis[i] = (stack[-1] - i, stack[-1]) # 거리, 인덱스
    stack.append(i)

# for i in range(n):
#     print(f"현재 탑 인덱스 : {i+1}, 개수 : {cnt[i]} , 현재 탑의 가장 가까운 번호 : {dis[i][1] + 1}")

for i in range(n):
    if cnt[i] == 0:
        print(0)
    else:
        print(f"{cnt[i]} {dis[i][1] + 1}")