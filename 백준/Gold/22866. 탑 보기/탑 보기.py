import sys

# 탑 보기
# 건물 n개, 각 건물 양 옆에 보이는 건물 수 구하는 문제
# 본인 높이보다 큰 건물만 볼 수 있다.
# n <= 100,000 -> N^2 안됨
# 각 건물에서 볼 수 있는 건물 개수 구하기,
# 만약 볼 수 있는 건물 여러개 -> 거리가 가장 가까운 건물의 번호 중 작은 번호


n = int(input())
heights = list(map(int, input().split())) # 건물들의 높이
# -> 보자마자 스택 떠올림
cnt = [0] * n
stack = []
INF = int(1e9)
nearest = [INF] * n # 가장 가까운 건물의 번호 저장
# 먼저 왼쪽에서 오른쪽으로 진행.
for i in range(n):
    now_height = heights[i] # 현재 건물 높이
    while stack and heights[stack[-1]] <= now_height: # 스택에서 건물의 인덱스 저장.
        stack.pop()
    cnt[i] += len(stack) # 본인보다 왼쪽에 있는 건물 중 높이 더 높은 건물 개수 저장
    if stack: # 본인보다 높은 건물이 있을 때만 갱신
        nearest[i] = stack[-1] # 현재 건물의 가장 가까운 인덱스 저장 (오른쪽에서 돌 때 비교 진행)
    stack.append(i)

# 오른쪽에서 왼쪽으로 진행
stack = []
for i in range(n-1, -1, -1):
    now_height = heights[i] # 현재 건물 높이
    while stack and heights[stack[-1]] <= now_height:
        stack.pop()
    cnt[i] += len(stack)
    # 이제 여기서 가장 가까운 건물의 인덱스 넘버 비교해야해.
    # 1. 거리가 가까운, 거리가 같다면 건물 번호가 더 작은
    # 현재 건물과 기존 저장된 가장 가까운 건물 거리와 현재 건물과 여기서의 가장 가까운 건물 거리 비교
    if stack:
        prev_dis = i - nearest[i]
        now_dis = stack[-1] - i
        if nearest[i] == INF: # 현재 가장 가까운 게 없다면
            nearest[i] = stack[-1]
        elif i - nearest[i] > stack[-1] - i: # 지금의 거리가 더 작은 경우에 교체
            nearest[i] = stack[-1]
        elif i - nearest[i] == stack[-1] - i: # 거리가 같은 경우
            nearest[i] = min(nearest[i], stack[-1]) # 더 작은 번호로 저장
    stack.append(i)

for i in range(n):
    if cnt[i] == 0:
        print(0)
    else:
        print(f"{cnt[i]} {nearest[i] + 1}")