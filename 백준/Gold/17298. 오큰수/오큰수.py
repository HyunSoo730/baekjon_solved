import sys
from collections import deque

# 크기가 N인 수열 A의 각 원소에 대해서 오큰수 NGE(i) 구하기
# 수열에서 i번째 수 Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미.
# 오큰수 없으면 -1
# N <= 10^6 N^2 X

n = int(input())
data = list(map(int, input().split()))
res = [-1] * n
stack = deque()
for i in range(n-1, -1, -1):
    now = data[i]
    while stack and stack[-1] <= now:
        stack.pop() # 현재 값이 스택 TOP 보다 같거나 크면 POP
    if stack:
        res[i] = stack[-1]
    else:
        res[i] = -1
    stack.append(now)

print(*res)