import sys
from collections import deque


n = int(input())
data = list(map(int, input().split()))
stack = []
res = []
for idx, val in enumerate(data):
    if len(stack) == 0: # 비어있으면
        stack.append((idx, val)) # 현재꺼 최신으로 저장
        res.append(0)
    elif stack[-1][1] > val: # 현재꺼보다 크면
        res.append(stack[-1][0]+1) # 마지막 인덱스 결과값에 저장
        stack.append((idx, val))
    elif stack[-1][1] < val: # 현재꺼보다 작으면
        while stack: # 스택이 존재할 때까지 반복
            if stack[-1][1] < val:
                stack.pop()
            else:
                res.append(stack[-1][0]+1)  # 해당 인덱스 저장하고
                stack.append((idx, val))
                break
        else:
            res.append(0)
            stack.append((idx,val))

for x in res:
    print(x, end = " ")