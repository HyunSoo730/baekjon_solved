import heapq

def solution(n, works):
    # 야근 피로도 : 야근 시작 시점에 남은 일의 작업량 제곱하여 더한 값
    # N시간 동안 야근 피로도 최소화하도록 일하기
    # 1시간에 작업량 1 처리
    # 남은 N시간, 각 작업량 works에 대해 야근 피로도 최소화 리턴
    # 결국 가장 작업 많이 남은 애들 줄여야함 -> 그리디적인 생각
    
    heap = []
    for x in works:
        heapq.heappush(heap, -x) # 최대힙으로 전환
    
    for _ in range(n): # n번 반복
        if heap[0] == 0: # 더이상 X
            return 0
        work = -heapq.heappop(heap)
        work -= 1 # 작업량 -1
        heapq.heappush(heap, -work)
    
    res = 0
    print(heap)
    while heap:
        work = -heapq.heappop(heap)
        res += work * work
    print(res)
    return res