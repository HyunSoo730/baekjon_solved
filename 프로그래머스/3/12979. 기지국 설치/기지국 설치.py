
def solution(n, stations, w):
    # N개의 아파트 일렬로 .
    # 일부 아파트 위에 기지국 존재 -> 기지국 교체
    # 기지국 최소로 설치하기.
    
    # 아파트 개수 n, 기존 설치되어있는 기지국 배열 stations, 범위 w
    # step1. 이미 커버된 구간 찾기
    # step2. 커버 안 된 구간 찾기
    # step3. 각 빈 구간마다 필요한 개수.. 찾기
    coverage = 2 * w + 1 # 기지국 하나의 범위
    pos = 1  # 현재 확인 중인 아파트 (시작 1)
    idx = 0 # 현재 확인 기지국 인덱스
    length = len(stations)
    
    res = 0

    while pos <= n: # 모든 아파트에 적용해야함.
        if idx < length and pos >= stations[idx] - w: # 기존 설치된 기지국 커버 범위 이내인가 ?
            pos = stations[idx] + w + 1 # 위치 조정 후
            idx += 1 # 다음 기지국 커버
        else: # 커버 안됨 -> 기지국 설치
            res += 1
            pos += coverage # 새 기지국 커버 끝으로 점프
    print(res)
    return res
    
    
    
    
    