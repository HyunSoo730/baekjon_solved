import heapq
from collections import deque

# 게단의 입구까지 이동하는 시간 + 계단을 내려가는데 걸리는 시간
# 각 계단 최대 3명
# 만약 3명 이용 중이라면 한 명이 계단을 다 내려갈 때까지 기다려야 한다.
#  먼저 각 사람 별로 어느 계단으로 갈지 부분집합.
# 그 후 계산 시작.
# step1
# 각 사람들 어느 계단으로 갈지 정한 후
# 모두 선택 후 시간 별로 정렬 각 계단별 큐에 넣어서 3명 이하면 가장 마지막 도착시간 + 1
# 3명이 넘어가면 첫번째에서 꺼내서 해당 사람과 새롭게 들어갈 사람 시간이 더 큰 사람 넣어주기

def DFS(L):
    global res
    if L == len(person): # 모든 사람 확인
        # 이제 각 계단 별로 확인
        dataA = []
        dataB = []
        for i in range(len(person)):
            if check[i] == 0: # 현재 사람은 첫번째 계단 선택
                t = abs(person[i][0] - stairs[0][0]) + abs(person[i][1] - stairs[0][1]) # 계단까지 도착하는 시간
                heapq.heappush(dataA, t) # 최소힙으로 저장
            else:
                t = abs(person[i][0] - stairs[1][0]) + abs(person[i][1] - stairs[1][1])
                heapq.heappush(dataB, t)

        # 각 사람별 계단에 도착한 시간을 작은 순서로 정렬하여 힙큐에 저장.
        resA = deque()
        resB = deque() # 계단을 오르는 사람을 저장할 배열
        while dataA:
            t = heapq.heappop(dataA)
            if len(resA) < 3: # 계단 오를 수 있으면 그냥 넣어
                resA.append(t)
            else: # 계단 오르는 사람 3명
                first = resA.popleft() # 가장 먼저 오르고 있는 사람을 꺼내서 해당 사람이 끝나느 시간과 새롭게 계단을 오르려는 사람의 시간 중 큰값으로 다시 넣어야함
                if first + stairs[0][2] > t: # 현재 오르고 있는 사람이 계단에 도착한 사람보다 크면 대기해야 하므로
                    resA.append(first + stairs[0][2]) # 첫번째 사람이 끝나는 시간이 현재 계단에 도착한 사람이 오르기 시작하는 시간이므로
                else:
                    resA.append(t)
        while dataB:
            t = heapq.heappop(dataB)
            if len(resB) < 3:
                resB.append(t) # 오를 수 있음
            else:
                first = resB.popleft()
                if first + stairs[1][2] > t:
                    resB.append(first + stairs[1][2])
                else:
                    resB.append(t)
        resultA = resultB = 0
        if len(resA) > 0:
            resultA = resA.pop() + stairs[0][2] + 1 # 1분 대기하는 시간까지 계산
        if len(resB) > 0:
            resultB = resB.pop() + stairs[1][2] + 1
        result = max(resultA, resultB)
        res = min(res, result)
    else:
        check[L] = 0 # 첫번째 계단으로 선택
        DFS(L+1)
        check[L] = 1 # 두번째 계단으로 선택
        DFS(L+1)

T = int(input())
for t in range(1,T+1):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    person = []
    stairs = []
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1: # 사람
                person.append((i,j)) # 사람 좌표
            if g[i][j] > 1: # 계단
                stairs.append((i,j, g[i][j])) # 계단 좌표, 계단 길이

    check = [0] * len(person)
    res = int(1e9) # 맥스로 설정
    DFS(0)
    print(f"#{t} {res}")