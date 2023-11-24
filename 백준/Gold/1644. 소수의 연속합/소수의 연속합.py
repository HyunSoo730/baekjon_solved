import math
import sys
from collections import deque


n = int(input())
data = [True] * (n+1) # 소수를 저장할 리스트
data[0] = False
data[1] = False # 0,1은 제외
for i in range(2, int(math.sqrt(n)) + 1):
    if data[i] == True: # True라면 그 배수들은 모두 소수가 아니야.
        j = 2
        while i * j <= n:
            data[i*j] = False # 배수는 모두 소수가 아니야
            j += 1

arr = [] # 소수 숫자를 저장할 배열
for i in range(n+1):
    if data[i] == True:
        arr.append(i)
# print(*arr)
# 소수 구했으니 이제 투 포인터로 계산해보기
e = 0 # s는 자동 증가
length = len(arr)
interval_sum = 0
cnt = 0
for s in range(length):
    while interval_sum < n and e < length:
        interval_sum += arr[e]
        e += 1
    if interval_sum == n:
        cnt += 1
    interval_sum -= arr[s]
    s += 1
print(cnt)

