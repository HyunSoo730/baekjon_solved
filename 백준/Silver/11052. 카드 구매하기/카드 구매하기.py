import sys


#8가지 색 존재
#카드 1~n개 포함된 카드팩. 카드팩 n가지 존재
#가격이 비싸면 높은 등급의 카드
#비싼걸로 사기 가치?? 조건 2개
#가방 문제랑 동일? 냅색 알고리즘

n = int(input())
data = list(map(int, input().split())) 
data.insert(0,0) #1번 인덱스부터 활용하기 위해
#data[i]는 i개의 카드를 사는데 data[i]값이 든다는 의미
dp = [0] * 1001
dp[1] = data[1] #자명한 사실.
#dp[i]는 i개의 카드를 사는데 드는 최댓값
for i in range(1,n+1):
    cnt = i   #개수
    val = data[i]  #가격
    for j in range(cnt, n+1):
        #현재 카드팩을 산다고 생각했을 때
        caseA = dp[j-cnt] + val
        caseB = dp[j]
        dp[j] = max(caseA, caseB)
print(dp[n])