import sys

# n개의 회의
# 각 회의는 시작시간, 끝나는 시간 주어짐. 기준 2개
# 회의가 겹치지 않게 하면서 회의실 사용할 수 있는 회의의 최대 개수
# 끝나는 시간 기준 정렬.
# n <= 100,000 N^2 안된다.
n = int(input())
data = []
for _ in range(n):
    start,end = map(int, input().split())
    data.append((start,end))

data.sort(key = lambda x : (x[1], x[0])) # 끝나는 시간 기준 정렬, 같으면 시작시간
end = data[0][1] # 가장 마지막 회의의 끝나는 시간과 비교해야 함.
cnt = 1
for i in range(1,n):
    if data[i][0] >= end:
        cnt += 1
        end = data[i][1]

print(cnt)