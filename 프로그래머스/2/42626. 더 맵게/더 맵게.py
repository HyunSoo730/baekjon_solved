import heapq
def solution(scoville, K):
    # 모든 음식 스코빌 지수 K 이상으로.
    # 가장 낮은 두 개의 음식 섞어 새로운 음식 만듦 -> 공식
    
    # 모든 음식의 스코빌 지수를 K이상으로 만들기 위해 섞어야 하는 최소 횟수
    
    heap = []
    for val in scoville:
        heapq.heappush(heap, val)
    res = 0
    def count_value(data):
        count = 0
        for val in data:
            if val < K:
                return False
        else:
            return True
    
    # step1. 가장 가까운 2개 꺼내기
    flag = False
    while not count_value(heap):
        if len(heap) < 2:
            flag = True
            break
        numA = heapq.heappop(heap)
        numB = heapq.heappop(heap)
        num = numA + numB * 2
        heapq.heappush(heap, num)
        res += 1
    
    if flag:
        res = -1
    return res
    
    
    