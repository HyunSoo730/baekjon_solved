def solution(n, times):
    # n명 입국심사, 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간 다름
    # 가장 앞에 있는 사람 
    # 1. 비어있는 심사대로 가거나
    # 2. 기다렸다가 더 빨리 끝나는 심사대로 가거나.
    # 모든 사람이 심사를 받는데 걸리는 최소 시간 구하기
    # 결정 문제... 특정 시간 범위에서. 모두 처리가 가능한지 생각.
    
    left,right = 1, max(times) * n + 1 # 최악의 경우.
    
    def is_possible(time_limit):
        cnt = 0 # 해당 시간동안 처리 가능한 인원.
        for i in range(len(times)):
            cnt += time_limit // times[i]
        return cnt >= n # 해당 시간동안 n명 가능한지.
    
    while left < right:
        mid = (left + right) // 2
        
        if not is_possible(mid): # 불가능하면.
            left = mid + 1 # 시간 늘려야함. 끝날 때 가능한 첫번째에서 멈춤.
        else:
            right = mid
    print(left)
    return left
            
    