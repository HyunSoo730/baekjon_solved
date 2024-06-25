import heapq

# 차량 정비소. 지갑 돌려주기
# 접수 창구번호, 정비 창구번호
# n개의 접수 창구, m개의 정비 창구
# 두 단계를 거쳐 차량 정비.
# 방문 -> 접수 창구 -> 정비 창구
# 각 접수 창구, 정비 창구의 처리 시간은 다르다.
# 차량 정비소 방문 고객 K명, 도착하는 순서대로.
# 차량 정비소 도착하면
# 1-1. 빈 접수 창구가 있는 경우 빈 접수 창구 이용
# 1-2. 빈 접수 창구가 없는 경우 빈 접수 창구가 생길 떄까지 대기
# 접수 창구 끝나고 정비 창구로 가면
# 2-1. 빈 정비 창구가 있는 경우 빈 정비 창구 이용
# 2-2. 빈 정비 창구가 없다면 빈 정비 창구가 생길 때까지 대기

# 접수 창구 우선순위
# 1. 여러 고객이 기다리는 경우 고객 번호가 낮은 순서대로 접수 창구 이용
# 2. 빈 접수 창구가 여러개라면, 접수 창구번호가 작은 곳으로 이동
# 여러 고객이 있는 경우, 빈 접수 창구가 여러개인 경우. 이럴 때를 생각하면서 문제를 생각해야함

# 정비 창구 우선순위
# 1. 접수 창구 끝나고 먼저 도착한 고객 우선
# 2. 여러 명의 고객이 동시에 오면. 이용했던 접수 창구번호 작은 고객 우선
# 3. 빈 정비 창구가 여러개라면 정비 창구번호 작은 곳으로
# 여러 고객이 있는 경우, 빈 정비창구가 여러개인 경우. 이럴 때를 생각하면서 문제 풀기

# 초기 주어지는 것 : 고객들의 차량 정비소 도착시간, 각 접수 창구 처리시간, 각 정비 창구 처리시간,
# 지갑을 분실한 고객과 같은 접수 창구와 같은 정비 창구를 이용한 고객 찾고 번호 합 구하기
# 그런 고객 없으면 -1 출력

T = int(input())
for t in range(1, T + 1):
    n, m, k, A, B = map(int, input().split())  # 접수창구 개수, 정비창구 개수, 고객 수, 잃어버린 고객이 사용한 접수창구, 정빛아구
    A -= 1
    B -= 1
    접수창구 = list(map(int, input().split())) # 접수창구 처리시간
    정비창구 = list(map(int, input().split())) # 정비창구 처리시간
    방문시간 = list(map(int, input().split())) # 각 고객 방문시간

    waiting_접수 = [] # 각 접수창구의 (끝나는 시간, 접수창구idx)를 우선순위큐로 저장
    waiting_정비 = [] # 각 정비창구의 (끝나는 시간, 정비창구idx)를 우선순위큐로 저장
    # step1. 각 접수창구를 (끝나는 시간, 접수창구idx)로 우선순위큐에 저장
    for i in range(n):
        heapq.heappush(waiting_접수, (0, i))

    users = [] # 접수창구 끝나는 고객들의 (끝나는 시간, 이용했던 접수창구idx, user_idx) 우선순위큐에 넣어둠
    for i in range(k): # 각 고객은 순서대로 들어오므로
        visit_time = 방문시간[i] # 현재 고객이 방문한 시간
        temp = [] # 현재 고객이 가능한 접수창구를 저장하기 위해
        while waiting_접수 and waiting_접수[0][0] <= visit_time: # 방문시간이 가장 빨리 끝나는 접수창구의 끝나는 시간보다 같거나 크면. 후보군
            end_time, idx_접수 = heapq.heappop(waiting_접수)
            heapq.heappush(temp, (idx_접수, end_time))
        if temp: # 이용 가능 접수 창구 여러개 -> 가장 접수창구번호 작은 거 이용
            idx_접수, end_time = heapq.heappop(temp)
            heapq.heappush(users, (visit_time + 접수창구[idx_접수], idx_접수, i)) # 접수창구 끝나는시간, 이용한 접수창구idx, 현재 고객의 인덱스
            heapq.heappush(waiting_접수, (visit_time + 접수창구[idx_접수], idx_접수))
        else: # 이용 가능 접수창구 없음 -> 대기. (가장 빨리 끝나는 접수창구 이용)
            end_time, idx_접수 = heapq.heappop(waiting_접수)
            heapq.heappush(users, (end_time + 접수창구[idx_접수], idx_접수, i))
            heapq.heappush(waiting_접수, (end_time + 접수창구[idx_접수], idx_접수))

        while temp: # 이용안한 거 다시 접수창구 대기에 넣어주기
            idx_접수, end_time = heapq.heappop(temp)
            heapq.heappush(waiting_접수, (end_time, idx_접수))

    # step2. 접수창구 끝난 유저들을 정비창구 이용시키기
    res =[]
    for i in range(m):
        heapq.heappush(waiting_정비, (0, i)) # 각 정비창구 끝나는 시간, 정비창구 인덱스
    while users:  # 먼저 도착한 고객들 한명씩 꺼내기 (우선순위큐에서 자연스럽게 접수창구번호 작은애들이 나옴)
        # 이제 그러면 빈 정비창구가 여러개일 때를 고려해야함
        end_time_접수, idx_접수, user_idx = heapq.heappop(users)
        temp = []
        while waiting_정비 and waiting_정비[0][0] <= end_time_접수: # 가장 먼저 끝나는 고객보다 정비창구 끝나는 시간이 같거나 작으면 모두 후보군
            end_time_정비, idx_정비 = heapq.heappop(waiting_정비)
            heapq.heappush(temp, (idx_정비, end_time_정비))
        if temp: # 빈 정비창구 있다면 가장 우선순위 높은 거 꺼내서 이용
            idx_정비, end_time_정비 = heapq.heappop(temp)
            res.append((user_idx, idx_접수, idx_정비))
            heapq.heappush(waiting_정비, (end_time_접수 + 정비창구[idx_정비], idx_정비))
        else: # 빈 정비창구 없으면 가장 빨리 끝나는 .
            end_time_정비, idx_정비, = heapq.heappop(waiting_정비)
            res.append((user_idx, idx_접수, idx_정비))
            heapq.heappush(waiting_정비, (end_time_정비 + 정비창구[idx_정비], idx_정비))

        while temp: # 사용 안한 거 다시.
            idx_정비, end_time_정비 = heapq.heappop(temp)
            heapq.heappush(waiting_정비, (end_time_정비, idx_정비))

    sum_idx = 0
    for user_idx, idx_접수, idx_정비 in res:
        if idx_접수 == A and idx_정비 == B:
            sum_idx += (user_idx +1)
    if sum_idx == 0:
        print(f"#{t} {-1}")
    else:
        print(f"#{t} {sum_idx}")
        


