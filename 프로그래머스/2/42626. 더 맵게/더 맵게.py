import heapq
def solution(scoville, K):
    # 모든 음식 스코빌 지수 K 이상으로.
    # 가장 낮은 두 개의 음식 섞어 새로운 음식 만듦 -> 공식
    
    # 모든 음식의 스코빌 지수를 K이상으로 만들기 위해 섞어야 하는 최소 횟수
    
    heapq.heapify(scoville) # O(N) : 한번에 힙 생성
    heap = scoville
    
    res = 0
    while heap[0] < K:
        if len(heap) < 2: # 더이상 안돼
            return -1
        
        #  두개 꺼내서 합치기
        numA = heapq.heappop(heap)
        numB = heapq.heappop(heap)
        heapq.heappush(heap, numA + numB * 2)
        res += 1
    
    print(res)
    return res
    
    
    
    