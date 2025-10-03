
def solution(routes):
    # 모든 차량이 단속용 카메라를 한번은 만나도록 카메라 설치.
    # 모든 차량이 한 번은 단속용 카메라 만나야 함... 최소 몇 대의 카메라가 필요한가 ?
    # 10^4
    # 최소 자원사용... 그리디 + 우큐로 가능한가 ?
    """
    단속 카메라 문제
    - 카메라 한 지점에 고정 설지
    - 여러 구간을 관통하는 점 찾기... -> 구간 커버 문제 
    - 끝점에 설치해야 최적
    """
    
    data = routes
    data.sort(key = lambda x : x[1])
    
    cnt = 1
    last_end_time = data[0][1]
    for start, end in data[1:]:
        if start > last_end_time:
            cnt += 1
            last_end_time = end # 갱신

    print(cnt)
    return cnt