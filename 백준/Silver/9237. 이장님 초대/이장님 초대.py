import sys


N = int(input())
data = list(map(int, input().split()))  #각 나무가 자라는데 걸리는 일

#각 묘목은 심는데 1일, 다 자라는데 걸리는건 개별
#나무를 심는 순서 정해서 최소날짜로 모두 자라게, 이장은 다음날에 초대
data.sort(reverse= True)  #내림차순
data.insert(0, 0) #1번 인덱스부터 사용.

max_date = 0
for idx, value in enumerate(data):
    if max_date < idx + value:
        max_date = idx + value

print(max_date + 1)   #나무가 다 자란 다음날 이장님 초대