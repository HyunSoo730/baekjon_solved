import sys


#2, 5원짜리로만 거스름돈
#동전개수 최소
N = int(input())

count = 0
while N > 0:
    if N % 5 == 0:
        count += N // 5
        break
    else:
        N -= 2     #5의 배수가 아니면 2원씩 빼서 5로 나누어떨어지는 것이 나올 때까지.
        count += 1
    
#반복문 탈출 후 0보다 작을 수도
if N < 0:
    print(-1)   #음수면 거슬러줄 수 없으니
else:
    print(count)    

