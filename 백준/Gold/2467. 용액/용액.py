import sys

N = int(input())
data = list(map(int, input().split()))

left = 0
right = N-1

res_left = -1
res_right = -1
res = 242424242424
while left < right:
    temp = data[left] + data[right]

    if temp == 0:
        res_left = data[left]
        res_right = data[right]
        break

    if abs(temp) < res:
        res = abs(temp)
        res_left = data[left]
        res_right = data[right]
    
    if temp > 0:
        right -=1
    else:
        left += 1

print(res_left, res_right)
