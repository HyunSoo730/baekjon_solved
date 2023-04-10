import sys


#기간, 금액
#N+1을 넘어가면 안됨.

n = int(input())
data = []
for _ in range(n):
    a,b = map(int, input().split())
    data.append((a,b)) #기간, 금액

data.insert(0,(0,0)) #1번 인덱스부터 사용하기 위해.
res = 0
def DFS(L, sum):
    global res
    if L >= n+1:  #n+1부터는 안돼. 종료조건
        if res < sum:
            res = sum
    else: #선택
        if L + data[L][0] <= n+1:
            DFS(L+data[L][0], sum + data[L][1]) #현재 요일 선택
        DFS(L+1, sum) #현재 요일 선택 x

DFS(1,0)
print(res)