import heapq

def solution(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x[0])  # 요청 시간을 기준으로 오름차순 정렬
    temp = []
    last = 0  # 가장 마지막 작업의 끝나는 시간
    res = 0
    cur_time = 0  # 현재 시간

    while jobs or temp:
        while jobs and jobs[0][0] <= cur_time:
            start, time = jobs.pop(0)
            heapq.heappush(temp, (time, start))  # 처리 시간, 요청 시각을 튜플로 힙에 삽입

        if temp:
            time, start = heapq.heappop(temp)
            last = cur_time
            cur_time = max(cur_time + time, start + time)
            res += cur_time - start
        else:
            cur_time = jobs[0][0]

    res //= n
    return res