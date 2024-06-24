import heapq

# 차량 정비소. 접수 창구번호, 정비 창구번호
# 차량 정비소에는 N개의 접수 창구, M개의 정비 창구
# 각 접수 창구, 정비 창구 처리 시간 다름.
# 차량 정비소 방문 고객 K명. 방문 순서대로 1~K
# 고객이 차량 정비소에 도착하면
# 1-1. 빈 접수 창구가 있는 경우 접수 창구에 가서 접수
# 1-2. 빈 접수 창구 없으면 생길때까지 대기
# 접수 창구 처리 끝나면
# 2-1. 빈 정비 창구 있는 경우 빈 정비 창구에 가서 차량 정비
# 2-2. 빈 정비 창구 없는 경우 빈 정비 창구 생길 때까지 대기

# 접수 창구 우선순위
# 1-1. 여러 고객 대기 -> 고객 번호 낮은 순서대로 우선 접수. -> 무조건 !!
# 1-2. 빈 창구 여러곳 -> 접수 창구 적은 곳으로 간다.

# 정비 창구 우선순위
# 2-1. 먼저 기다리는 고객 우선 (접수 창구 먼저 끝난 사람 우선)
# 2-2. 두 명 이상 고객들이 접수 창구에서 동시 접수 완료 -> 이용했던 접수 창구 번호 작은 고객 우선
# 2-3. 빈 창구 여러 곳 -> 정비 창구번호 작은 곳으로 간다.

# 원하는 고객과 같은 접수 창구, 정비 창구를 이용한 고객이 없다면 -1 출력

T = int(input())
for t in range(1,T+1):
    n,m,k,A,B = map(int, input().split())
    A -= 1
    B -= 1
    접수창구 = list(map(int, input().split())) # 각 접수 창구 처리 시간
    정비창구 = list(map(int, input().split())) # 각 정비 창구 처리 시간
    방문시간 = list(map(int, input().split())) # 각 고객이 차량 정비소 방문 시간

    # step1. 방문시간 + 접수 창구 우선순위.
    heap = []
    for i in range(k):
        heapq.heappush(heap, (i,방문시간[i])) # 접수 창구 우선순위는 고객 번호 낮은 순.
    # 방문시간 순으로 일단 힙에 넣어둠.
    heapA = [] # 접수 창구
    heapB = [] # 정비 창구
    users = [] # 접수 창구 끝나는 사람 정보 기입 위해. (이후에 정비 창구 들어가기 위해)
    for i in range(n):
        heapq.heappush(heapA, (0,i)) # 해당 접수창구가 끝나는 시간, 접수 창구 번호 낮은 순
    for i in range(m):
        heapq.heappush(heapB, (0,i)) # 해당 정비창구가 끝나는 시간, 해당 정비창구 번호 낮은 순
    while heap: # 방문시간 빠른순 (번호 낮은 순으로 꺼내서) 한명씩 확인
        user_idx, visit_time = heapq.heappop(heap) # 차량 정비소 방문 고객 idx, 해당 고객 방문 시간
        temp = [] # 매 순간 갱신 ?
        # 빈 창구 찾기
        while heapA and heapA[0][0] <= visit_time:
            end_time_A, idx_A = heapq.heappop(heapA)
            heapq.heappush(temp, (idx_A, end_time_A)) # 방문시간으로 갱신해야지 !

        if temp: # 빈 창구 있으면
            idx_A, end_time_A = heapq.heappop(temp)
            heapq.heappush(users, (visit_time + 접수창구[idx_A], idx_A, user_idx))
            heapq.heappush(heapA, (visit_time + 접수창구[idx_A], idx_A))
        else: # 빈 창구 없으면
            end_time_A, idx_A = heapq.heappop(heapA)
            heapq.heappush(users, (end_time_A + 접수창구[idx_A], idx_A, user_idx))
            heapq.heappush(heapA, (end_time_A + 접수창구[idx_A], idx_A))
        # heapA에 다시 temp 요소 추가
        while temp:
            idx_A, end_time_A = heapq.heappop(temp)
            heapq.heappush(heapA, (end_time_A, idx_A))

    # step2. 먼저 온 순서대로 정비 창구.
    result = []
    while users:
        end_time, idx_A, user_idx = heapq.heappop(users) # 접수 창구 끝난 시간, 해당 접수창구 넘버, 현재 유저 넘버
        temp = []
        while heapB and heapB[0][0] <= end_time:
            end_time_B, idx_B = heapq.heappop(heapB)
            heapq.heappush(temp, (idx_B, end_time_B))

        if temp: # 빈 창구가 있으면
            idx_B, end_time_B = heapq.heappop(temp)
            result.append((user_idx, idx_A, idx_B))
            heapq.heappush(heapB, (end_time + 정비창구[idx_B], idx_B))
        else: # 빈 창구가 없으면
            end_time_B, idx_B = heapq.heappop(heapB)
            result.append((user_idx, idx_A, idx_B))
            heapq.heappush(heapB, (end_time_B + 정비창구[idx_B], idx_B))

        while temp:
            idx_B, end_time_B = heapq.heappop(temp)
            heapq.heappush(heapB, (end_time_B, idx_B))

        # end_time_B, idx_B = heapq.heappop(heapB)
        # if end_time >= end_time_B:
        #     result.append((user_idx, idx_A, idx_B))
        #     heapq.heappush(heapB, (end_time + 정비창구[idx_B], idx_B))
        # else:
        #     result.append((user_idx, idx_A, idx_B))
        #     heapq.heappush(heapB, (end_time_B + 정비창구[idx_B], idx_B))


    sum_idx = 0
    for user_idx, idx_A, idx_B in result:
        if idx_A == A and idx_B == B:
            sum_idx += (user_idx + 1)

    if sum_idx == 0:
        print(f"#{t} {-1}")
    else:
        print(f"#{t} {sum_idx}")

