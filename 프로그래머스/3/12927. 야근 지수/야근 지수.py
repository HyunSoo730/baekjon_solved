import heapq

def solution(n, works):
    # 야근 지수.
    # 야근을 하면 피로도가 쌓인다. 
    # 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업략을 제곱하여 더한 값.
    # 야근 피로도 = 시작 시점 + 작업량**2
    
    # N시간 동안 야근 피로도 최소화하도록 일하기
    # 1시간 동안 작업량 1만큼 처리할 수 있다
    # 퇴근까지 남은 N시간과 각 일에 대한 작업량 works에 대해 야근 피로도 최소화한 값을 리턴하는 함수
    
    # works <= 20,000 -> N^2 안됨
    heap = []
    for i in range(len(works)):
        time = works[i]
        heapq.heappush(heap, -time)
    
    for i in range(n):
        if heap:
            time = -heapq.heappop(heap)
            time -= 1
            if time > 0:
                heapq.heappush(heap, -time)
        else:
            break
    
    res = 0
    while heap:
        time = -heapq.heappop(heap)
        res += time ** 2
    print(res)
    return res
        
        
        
    