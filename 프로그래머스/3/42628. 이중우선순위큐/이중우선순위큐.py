import heapq
from collections import Counter
def solution(operations):
    # 이중 운선순위 큐가 할 연산 존재.
    # 모든 연산 처리 후 큐가 비어 있다면 [0,0] 비어있지 않으면 [최댓값, 최솟값] return
    
    max_heap = [] # 최대힙 
    min_heap = [] # 최소힙
    counter = Counter()
    for oper in operations:
        cmd, num_str = oper.split()
        num = int(num_str)
        if cmd == "I":
            # 개수 1개 추가 및 최대힙, 최소힙 추가 
            counter[num] += 1
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif cmd == "D":
            if num_str == "1": # 최댓값 삭제
                # step1. 유령데이터 삭제
                while max_heap and counter[-max_heap[0]] == 0: # 최대힙에 쌓여있는게 유령데이터라면 전부 지워야함
                    heapq.heappop(max_heap)
                # step2. 실제 최댓값 삭제
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    counter[max_val] -= 1
                
            elif num_str == "-1":
                # step1. 유령데이터 삭제
                while min_heap and counter[min_heap[0]] == 0: # 최소힙에 쌓여있는게 유령데이터라면 전부 지워야함
                    heapq.heappop(min_heap)
                # step2. 실제 최솟갑 삭제
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    counter[min_val] -= 1
        
    # 다 끝난 이후에도 유령 데이터 있을 수 있으므로 제거해줘야함
    while max_heap and counter[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and counter[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    if len(max_heap) == 0 and len(min_heap) == 0:
        return [0,0]
    else:
        return[-max_heap[0], min_heap[0]]