import sys


#J개의 사탕을 가게에 보내기 위해 상자에 포장
#크기가 다른 N개의 상자 상자 최소한으로 사용

T = int(input())
for _ in range(T):
    J, N = map(int, input().split()) #사탕의 개수, 상자의 개수
    data = []
    for i in range(N):
        row, col = map(int, input().split())  #세로, 가로
        data.append(row * col)  #튜플 형태로 저장
        #row * col만큼보다 더 많은 사탕을 포장할 수 없다.
    #모든 상자를 다 넣었으면 이제 가장 큰것들부터
    count = 0
    data.sort(reverse=True)
    for i in range(N):
        J = J - data[i]
        count += 1
        if J <= 0:
            break
    print(count)