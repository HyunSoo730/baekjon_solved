import heapq

# 차량 정비소
# 접수 창구번호, 정비 창구번호 존재
# N개의 접수 창구, M개의 정비 창구
# 먼저 접수 창구에서 처리 후 정비창구 이동
# 차량 정비소에 방문한 고객 K명
# 도착 순서대로 1번부터 부여받음

# 차량 정비소 도착
# 1-1. 빈 접수 창구가 있는 경우 빈 접수 창구에서 접수
# 1-2. 빈 접수 창구가 없는 경우 생길 때까지 대기

# 정비 창구 도착
# 2-1. 빈 정비창구가 있는 경우 빈 정비 창구에 가서 차량 정비
# 2-2. 빈 정비 창구가 없는 경우 정비창구가 생길 떄까지 대기

# 접수 창구 우선순위
# 1. 여러 고객 대기 시 고객번호가 낮은 순서대로 우선 접수
# 2. 빈 창구가 여러 곳인 경우 접수 창구번호가 작은 곳으로 이동

# 정비 창구 우선순위
# 1. 먼저 기다리는 고객 우선
# 2. 두명 이상 고객이 동시에 도착하면 이용했던 접수 창구 번호가 작은 고객 우선
# 3. 빈 창구 여러곳이면 정비 창구 작은곳으로 이동

# 초기 :
# 고객들의 도착시간, 접수 창구 처리 시간, 정비 창구 처리 시간 주어짐

# 구하고자 : 지갑을 두고 간 고객과 같은 접수 창ㅇ구 A와 같은 정비창구 B를 이용한 고객들의 고객 번호 합

T = int(input())
for t in range(1,T+1):
    n,m,k,A,B = map(int, input().split()) # 접수창구 수, 정비창구 수, 고객 수
    A -= 1
    B -= 1
    접수창구 = list(map(int, input().split())) # 각 접수창구 처리시간
    정비창구 = list(map(int, input().split())) # 각 정비창구 처리시간
    도착시간 = list(map(int, input().split())) # 각 고객의 도착시간

    heapA = []
    for i in range(n):
        heapq.heappush(heapA, (0,i)) # 각 접수창구의 (끝나는 시간, 접수창구번호) 로 초기화
    heapB = []
    for i in range(m):
        heapq.heappush(heapB, (0,i)) # 각 정비창구의 (끝나는 시간, 정비창구번호)로 초기화

    # 각 고객 순서대로 진행
    temp = []
    users = [] # 접수창구를 이용한 고객들
    for i in range(k):
        time = 도착시간[i] # 현재 고객의 도착시간
        while heapA and heapA[0][0] <= time: # 끝나는시간이 도착시간보다 작으면 바로 진행 가능
            end_time, idx = heapq.heappop(heapA) # 해당 접수 (끝나는 시간,접수번호)
            heapq.heappush(temp, idx) # 어차피 접수 번호만 알면 돼

        if temp: # 이용 가능한 접수창구 존재 -> 번호 낮은 애들 순으로 저장 중.
            idx = heapq.heappop(temp)
            end_time = time + 접수창구[idx] # 현재 고객이 접수창구가 끝나는 시간
            heapq.heappush(users, (end_time, idx, i)) # (접수 창구 끝나는 시간, 접수창구번호, 현재 이용한 고객 인덱스)
            heapq.heappush(heapA, (end_time, idx))
        else: # 이용 가능한 접수창구 없으면..
            end_time, idx = heapq.heappop(heapA) # 가장 빨리 끝나는 접수창구
            end_time += 접수창구[idx] # 가장 먼저 끝나는 접수창구 시간 + 접수창구 시간
            heapq.heappush(users, (end_time, idx, i))
            heapq.heappush(heapA, (end_time, idx))
    # 정비창구 시작
    temp = []
    res = []
    while users: # 먼저 도착한 순서대로 꺼내서 진행 -> 도착 시간 같은 경우 접수창구 번호 우선
        end_timeA, idxA, userIdx = heapq.heappop(users)

        while heapB and heapB[0][0] <= end_timeA: # 정비창구 끝나는 시간이 더 빠르면 바로 가능
            _, idxB = heapq.heappop(heapB) # 정비창구 끝나는 시간, 정비창구 번호
            heapq.heappush(temp, idxB)

        if temp: # 이용 가능한 정비창구 존재
            idxB = heapq.heappop(temp)
            end_timeB = end_timeA + 정비창구[idxB]  # 정비창구 끝나는 시간
            heapq.heappush(heapB, (end_timeB, idxB))
            res.append((userIdx, idxA,idxB))
        else: # 이용 가능한 정비 창구가 없다면
            end_timeB, idxB = heapq.heappop(heapB) # 가장 먼저 끝나는 정비창구, 인덱스
            end_timeB += 정비창구[idxB]
            heapq.heappush(heapB, (end_timeB, idxB))
            res.append((userIdx, idxA,idxB))


    sum_idx = 0
    for userIdx, idxA,idxB in res:
        if idxA == A and idxB == B:
            sum_idx += (userIdx+1)

    if sum_idx == 0:
        print(f"#{t} {-1}")
    else:
        print(f"#{t} {sum_idx}")





