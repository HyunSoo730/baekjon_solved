import sys


N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    data = list(map(int, input().split()))

    cnt = 1   #처음부터 담는다는 가정하에 1부터 줘야지
    sum = 0

    for i in range(N):
        if sum + data[i] > M:
            cnt +=1 
            sum = data[i]
        else:
            sum += data[i]

    print(cnt)
