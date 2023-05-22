import sys
from collections import deque

data = input()
res = 0
stack = []
flag = 0
temp = 1
for i in range(len(data)):
    if data[i] == "(":
        stack.append(data[i])
        temp *= 2
    elif data[i] == "[":
        stack.append(data[i])
        temp *= 3
    elif data[i] == ")":
        if not stack or stack[-1] == "[":
            res = 0
            break
        if data[i-1] == "(":
            res += temp
        stack.pop()
        temp = temp // 2
    elif data[i] == "]":
        if not stack or stack[-1] == "(":
            res = 0
            break
        if data[i-1] == "[":
            res += temp
        temp = temp // 3
        stack.pop()

if stack:
    res = 0
print(res)
