import heapq
def solution(A, B):
    # 각 사원 딱 한번 경기, 각 사원은 무작위 자연수 부여받고...
    # A 한명, B 한명 나와서 서로 수 공개. 숫자 큰 쪽이 승리 -> +1, 동점이면 0
    # 10^5 -> N^2 불가
    # A배열은 고정, B가 이길 수 있는 방법 생각
    # 둘 다 오름차순 정렬 후에...
    res = 0
    A.sort()
    B.sort()  # 둘 다 오름차순
    """
    A : 1 7 8 9 11
    B : 2 2 6 10 13
    temp = [2,6]
    """
    n = len(A)
    heapq.heapify(B)
    temp = [] # 만약 꺼낸게 A의 가장 작은 것보다 작을 경우 -> 버리는 카드 용으로 저장해놔야함.
    for i in range(n):
        if B and A[i] < B[0]: # 큰 경우
            res += 1
            heapq.heappop(B)
        else: # 동점이거나 작아 -> 버리는 카드 용 중에 가장 작은 거 버리기
            while B and B[0] <= A[i]:
                num = heapq.heappop(B)
                heapq.heappush(temp, num) # 임시 저장소에 저장.
            if B and A[i] < B[0]:
                res += 1
                heapq.heappop(B)
            else: # 더이상 없으므로 가장 작은 값 버려서 해결
                heapq.heappop(temp)
    print(res)
    return res