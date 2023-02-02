import sys


S = int(input())  #서로 다른 자연수 N개의 합
#N의 최댓값
N = 1   
while True:
    sum = N * (N+1) / 2
    if sum > S:
        break
    N += 1
#sum보다 커지면 N-1개로 S를 만들 수 있음 
print(N-1)
