def solution(A, B):
    A.sort()  # A 오름차순
    B.sort()  # B 오름차순
    
    answer = 0
    j = 0  # A의 포인터
    """
    A: 1 3 5 7
    B : 2 2 6 8
    """
    for num in B:
        if A[j] < num:
            answer += 1
            j += 1  # 매칭 되어 다음으로 넘어감.
    
    
    
    return answer