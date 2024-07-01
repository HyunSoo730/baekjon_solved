def solution(brown, yellow):
    # 노란색, 갈색 격자 개수는 기억하지만, 전체 카펫의 크기는 기억하지 못한다.
    # 갈색, 노란색 개수가 주어지면 가로, 세로 개수 반환하기
    # 가로, 세로 변수로 두고 문제 풀면 해결 가능.
    a = brown
    b = yellow
    total = a + b
    
    # 가능한 가로, 세로 조합 찾기
    for x in range(3, total // 2 + 1):
        if total % x == 0:
            y = total // x
            
            # 조건 확인
            if x >= y and (x-2) * (y-2) == b:
                return [x, y]
    
    # 없는 경우 
    return None