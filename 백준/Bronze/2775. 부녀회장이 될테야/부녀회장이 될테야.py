import sys


T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input()) #k층 n호
    data = list(range(1,n+1)) #0층 리스트 1~n명씩 산다.
    for i in range(k):
        for j in range(1,n):
            data[j] += data[j-1] #a층 b호에는 a-1층 1~b까지의 합 있어야 함.
    print(data[-1]) #k층 n호에 모두 저장될꺼야.