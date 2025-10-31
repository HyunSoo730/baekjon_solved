def solution(numbers, target):
    # n개의 정수.
    # 순서 안 바꾸고 더하거나 빼서 타겟넘버 만들기.
    n = len(numbers) # 개수
    cnt = 0
    def dfs(L, current_sum):
        nonlocal cnt
        if L == n: # 종료조건
            if current_sum == target:
                cnt += 1
        else: # 마지막 도달이 아니라면 선택해야함. 속하거나 속하지 않거나
            dfs(L+1, current_sum + numbers[L]) # 현재 순서 더함
            dfs(L+1, current_sum - numbers[L])
    
    dfs(0,0)
    print(cnt)
    return cnt