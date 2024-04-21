import heapq
import sys

# 길이가 n인 수열, 그 수열의 합 구하기
# 수열의 두 수를 묶어서 곱한 후 더함
# 수열의 각 수를 적절히 묶었을 때 합이 최대
# 곱한거랑 그냥 더한거랑 뭐가 더 큰지 판단해서 이어가면 될 듯
# 정렬 : 3 2 1 -1
# 3*2 3+2 -> 3*2 채택 : 6
# 1*-1, 1-1 -> 1-1 채택 : 0
# 이미 묶은 애는 더이상 묶을 수 없음

n = int(input())
plus = [] # 양수 저장
minus = [] # 0이하 저장

for _ in range(n):
    num = int(input())
    if num > 0: heapq.heappush(plus, -num) # 양수는 내림차순
    else: heapq.heappush(minus, num) # 음수는 오름차순

temp = []
res = 0
while len(plus) > 1:
    numA = -heapq.heappop(plus)
    numB = -heapq.heappop(plus)
    if numA * numB > numA + numB:
        res += numA * numB
    else:
        res += numA + numB
if plus:
    temp.append(-heapq.heappop(plus))

while len(minus) > 1:
    numA = heapq.heappop(minus)
    numB = heapq.heappop(minus)
    if numA * numB > numA + numB:
        res += numA * numB
    else:
        res += numA + numB
if minus:
    temp.append(heapq.heappop(minus))
while len(temp) > 1:
    numA = heapq.heappop(temp)
    numB = heapq.heappop(temp)
    if numA * numB > numA + numB:
        res += numA * numB
    else:
        res += numA + numB
if temp:
    res += heapq.heappop(temp)
print(res)