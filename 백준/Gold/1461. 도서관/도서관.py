import sys
from collections import deque

#책을 모두 제자리에 놔둘 때 최소 걸음
N, M = map(int, input().split())
data = list(map(int, input().split()))

left = []
right = []
max_data = 0
for x in data:
    if x < 0:
        left.append(x)
    else:
        right.append(x)

    if abs(x) > abs(max_data):
        max_data = x #마지막 책 저장 ### 값으로 저장했어야 !!
        
#양수는 내림차순, 음수는 오름차순
left.sort()
right.sort(reverse = True)

res = 0 #최소 걸음
#M권 들고 가는거면 M권 중에 가장 먼 거리까지 가는데 이전 책들 다 놓을 수 있다는거 생각했어야 했음
for i in range(0, len(left), M): #M씩 커져야지
    if left[i] != max_data:
        res += abs(left[i])

for i in range(0, len(right), M):
    if right[i] != max_data:
        res += abs(right[i])

#M권 놓고 항상 제자리로 돌아와야 하므로 와복.
res = res * 2
res +=  abs(max_data) #가장 먼 곳은 놓고 끝이니까
print(res)

            
            
            
            
            
