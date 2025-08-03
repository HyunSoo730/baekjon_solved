
import heapq
# N개의 접수 창구, M개의 정비 창구, K명의 고객
# 차량 정비소에서 2 단계를 거쳐 고객 차량 정비
# 고객은 도착하는대로 순서 부여. 고객은 도착하는 시간 존재

# 고객이 차량 정비소 도착하면
# 1-1. 빈 접수 창구가 있는 경우 빈 접수 창구 사용
# 1-2. 빈 접수 창구가 없는 경우, 빈 접수 창구 생길 때까지 대기.
# # 접수 창구 종류 후 정비 창구 이동
# 2-1. 빈 정비 창구 있는 경우, 빈 정비 창구 사용
# 2-2. 빈 정비 창구 없는 경우, 빈 정비 창구 생길 때까지 대기

# 접수 창구 우선순위
# 1. 여러 고객 대기 -> 고객번호가 낮은 순서대로 우선 접수
# 2. 빈 창구가 여러 곳 -> 창구 번호 작은 곳으로.
# 정비 창구 우선순위
# 1. 먼저 기다리는 고객 우선
# 2. 두 명 이상의 고객들이 접수 창구에서 동시에 접수 완료 후 정비 창구 도착 시
# -> 이용했던 접수 창구번호 작은 고객 우선
# 3. 빈 창구가 여러 곳인 경우 정비 창구번호 작은 곳으로 이동

# 고객의 도착시간, 접수 창구 처리시간, 정비 창구 처리시간 주어짐
# 지갑을 분실한 고객과 같은 접수 창구와 같은 정비 창구를 이용한 고객의 고객번호 찾아 그 합 출력 (없으면 -1)
T = int(input())
for t in range(1,T+1):
    n,m,k,A,B = map(int, input().split()) # 접수창구 개수, 정비창구 개수, 고객 수, 지갑 두고 간 고객이 이용한 접수 창구번호 A, 정비 창구번호 B
    접수창구 = list(map(int, input().split())) # 각 접수창구의 걸리는 시간
    정비창구 = list(map(int, input().split())) # 각 정비창구의 걸리는 시간
    고객방문시간 = list(map(int, input().split())) # 순서대로 주어짐

    # step1. 접수창구, 정비창구의 끝나는시간, 인덱스 세팅
    heapA = []
    for i in range(n):
        heapq.heappush(heapA, (0,i)) # 각 접수창구의 (끝나는시간, 접수창구 번호)로 초기화
    heapB = []
    for i in range(m):
        heapq.heappush(heapB, (0,i)) # 각 정비창구의 (끝나는시간, 정비창구 번호)로 초기화

    # step2. 도착한 순서대로 진행
    temp = [] # 현재 접수창구보다 먼저 도착한 고객들을 담아둘 리스트
    users = []  # 접수창구를 이용하고, 정비창구를 이용하기 전 우선순위대로 담아둘 리스트
    for i in range(k):
        time = 고객방문시간[i] # 현재 고객의 도착 시간
        while heapA and heapA[0][0] <= time: # 현재 가장 빨리 끝나는 접수창구의 끝나는 시간이 고객의 도착시간보다 먼저라면. 고객은 바로 사용 가능
            endTime, idx = heapq.heappop(heapA)  # 접수창구 끝나는 시간, 접수창구 번호
            heapq.heappush(temp, idx) # 가능한 접수창구의 번호를 적재

        if temp: # 이용 가능한 접수 창구 존재 -> 번호 낮은 거 이용
            idx = heapq.heappop(temp)
            endTime = time + 접수창구[idx] # 현재 고객이 접수창구 끝나는 시간
            heapq.heappush(users, (endTime, idx, i)) # 접수창구 끝나는 시간이 작은. 우선, 그 다음은 접수창구 번호가 적은 것 우선
            heapq.heappush(heapA, (endTime, idx)) # 해당 접수창구 사용하니 다시 끝나는 시간 갱신.
        else: # 이용 가능한 접수 창구 없음 -> 기다렸다가 이용 : 가장 빨리 끝나는 접수 창구의 시간에서 시작
            endTime, idx = heapq.heappop(heapA)
            endTime += 접수창구[idx]
            heapq.heappush(users, (endTime, idx, i))
            heapq.heappush(heapA, (endTime, idx))

    res = []
    temp = []
    # step3. 정비창구 시작
    while users: # 접수창구 먼저 끝난 사람부터 꺼내기
        endTimeA, idxA, i = heapq.heappop(users) # 접수창구가 끝나는 시간, 접수창구 번호, 고객의 인덱스

        while heapB and heapB[0][0] <= endTimeA:
            _, idxB = heapq.heappop(heapB)
            heapq.heappush(temp, idxB) # 정비창구 번호

        if temp: # 현재 고객이 바로 이용 가능한 정비창구 존재
            idxB = heapq.heappop(temp)
            endTimeB = endTimeA + 정비창구[idxB]
            heapq.heappush(heapB, (endTimeB, idxB))
            res.append((i, idxA, idxB)) # 고객번호 i가 이용한 접수창구번호, 정비창구번호 res 리스트에 저장
        else: # 현재 고객이 바로 이용 X -> 가장 빨리 끝나는 접수창구 시간 기준
            endTimeB, idxB = heapq.heappop(heapB)
            endTimeB += 정비창구[idxB]
            heapq.heappush(heapB, (endTimeB, idxB))
            res.append((i, idxA, idxB))

    # 최종 계산 시작
    sumIdx = 0
    for i, idxA, idxB in res:
        if idxA + 1 == A and idxB + 1 == B:
            sumIdx += (i+1)

    if sumIdx > 0:
        print(f"#{t} {sumIdx}")
    else:
        print(f"#{t} {-1}")



















