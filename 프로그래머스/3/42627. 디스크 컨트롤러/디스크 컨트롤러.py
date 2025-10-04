import heapq
def solution(jobs):
    # 하드디스크는 한 번에 하나의 작업만 수행.
    # 우선순위 존재
    # 작업 : 작업 번호, 요청 시각, 소요 시간 가지고 있음
    # 하드디스크가 작업 안하고 있으면 가장 우선순위가 높은 작업 진행
    # 1. 소요시간 짧고, 요청 시각 빠르고, 작업 번호 작은 것 순으로 우선순위
    # 구하고자 : 요청 작업의 반환 시간의 평균 구하기
    # 각 작업 : 요청시각 ~ 끝나는 시각
    # jobs에 요청시점, 소요시간 담겨져 있음
    heap = []
    res = 0
    idx = 0
    cnt = 0
    cur_time = 0
    n = len(jobs)
    jobs.sort()
    while cnt < n: #  # 모두 완료해야함
        # step1. 현재 요청시각 기준으로 가능한 애들 모두 추출
        while idx < n and jobs[idx][0] <= cur_time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0], idx))
            idx += 1
        # step2. 현재 시간에서 가능한 작업 진행
        if heap:
            # 가장 짧은 작업 처리
            timeB, timeA, _ = heapq.heappop(heap) # 소요시간, 요청시각
            cur_time += timeB # 현재시간 수정
            res += (cur_time - timeA)
            cnt += 1 # 하나 해결 
        else:
            # 현재 가능한 경우가 없으면 현재시간 변경
            if idx < n:
                cur_time = jobs[idx][0]
    print(res // n)
    return res // n
    
        
        
        
        
    