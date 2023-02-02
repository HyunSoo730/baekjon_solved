import sys
from collections import deque
import heapq as hq

# input = sys.stdin.readline

# 자료구조

N, M = map(int, input().split())
know = list(map(int, input().split()))[1:] #진실을 하는 사람의 수는 필요 없으니 슬라이싱.

visit = [0] * N
for i in know:
    visit[i-1] = 1  #1부터 시작이라 + 아는 사람들은 1로 표기


#파티 해당 데이터에 know의 인덱스가 포함되어 있다면 그 파티 구성원은 거짓말을 할 수 없음

party = []
for _ in range(M):
    temp = list(map(int, input().split()))[1:]
    party.append(temp)

party_visit = [0] * M #진실을 말해야 하는 파티는 1로 표기

#스택이 빌 때까지 반복
while know:
    know_person = know.pop()

    data = set()  #진실을 아는 pop된 사람들과 같은 파티에 있는 사람들 담을려고

    #pop된 사람과 같은 파티에 있는 사람들을 찾아 집합에 추가
    for i in range(len(party)):
        temp = set(party[i])  #각 파티별로 중복 제거
        if know_person in temp: #pop된 사람이 현재 파티일 경우
            data = data.union(temp)  #현재 파티 사람들 집합에 추가
            party_visit[i] = 1 #현재 파티를 진실을 말해야 하는 파티라고 표기
    
    #찾은 사람들 중 스택에 추가된 적이 없는 사람들을 스택에 추가
    for i in data:  #진실을 아는 사람들 중에 스택에 없으면 추가
        if visit[i-1] == 0:
            know.append(i) #해당 인덱스 안다고 표시
            visit[i-1] = 1   

print(party_visit.count(0))



    