import heapq
def solution(jobs):
    # 하드디스크는 한 번에 하나의 작업만 수행 가능
    # 각 작업은 작업 번호, 작업 요청 시각, 작업 소요 시간 존재
    # 가장 우선순위 높은 거 꺼내서 작업..
    # 우선순위 1. 소요시간 짧은, 2. 요청시각 빠른, 3. 작업 번호 작은.
    
    heap = []
    cnt = 0 # 모두 완료해야함
    cur_time = 0 # 현재시간 
    jobs.sort(key = lambda x : x[0]) # 우선 요청시점 기준으로 정렬 진행. 
    idx = 0 # 불가능한 경우를 생각해서 
    res = 0
    n = len(jobs)
    while cnt < n:
        while idx < n and jobs[idx][0] <= cur_time: # 현재시간 이라면 추출 가능
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0], idx))
            idx += 1
        
        if heap: # 가능하다면 가장 빠른걸로
            timeB, timeA, _ = heapq.heappop(heap) # 소요시간, 요청시각, 인덱스
            cur_time += timeB # 현재시간 변경
            res += (cur_time - timeA) # 반환 시간은 종료시간 - 요청시각
            cnt += 1 # 해결 개수 추가 
        else: # 없으면 가장 빠른 인덱스의 시간대로 이동
            if idx < n: # 물론 인덱스 내에서 
                cur_time = jobs[idx][0]
            
    print(res // n)
    return res // n
    
            
        