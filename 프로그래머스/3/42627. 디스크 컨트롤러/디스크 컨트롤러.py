import heapq

def solution(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x[0])  # 요청 시간을 기준으로 오름차순 정렬
    
    current_time = 0
    total_time = 0
    waiting_queue = []
    
    while jobs or waiting_queue:
        while jobs and jobs[0][0] <= current_time:
            request_time, processing_time = jobs.pop(0)
            heapq.heappush(waiting_queue, (processing_time, request_time))
        
        if waiting_queue:
            processing_time, request_time = heapq.heappop(waiting_queue)
            current_time += processing_time
            total_time += current_time - request_time
        else:
            current_time = jobs[0][0]
    
    return total_time // n