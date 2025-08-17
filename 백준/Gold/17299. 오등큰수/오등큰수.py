import sys
from collections import defaultdict, Counter, deque

# 크기 N인 수열 A -> 각 값의 오등큰수 구하기
# 오등큰수
# 1. Ai보다 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수
# 없으면 -1 출력
# 즉, Ai보다는 오른쪽에 있을 것, F(Ai) 보다 오른쪽에 있는 Ax의 등장횟수 F(Ax)가 더 클 것.
# N <= 10^6
n = int(input())
data = list(map(int, input().split()))

cnt = Counter(data) # 등장 횟수 계산 - O(N)
# Counter 사용 안할 시에 딕셔너리 사용이 깔끔
"""
cnt = defaultdict(int)
for num in data:
    cnt[num] += 1
"""
res = [-1] * n
stack = deque()
for i in range(n-1, -1, -1):
    now = data[i]
    while stack and cnt[stack[-1]] <= cnt[now]:
        stack.pop()
    if stack:
        res[i] = stack[-1]
    stack.append(now)

print(*res)
