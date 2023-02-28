import itertools
def solution(k, dungeons):
    #피로도 k
    #각 던전별 최소 필요도, 소모 피로도 2차원 배열로 주어짐
    data = dungeons
    #유저가 탐험할 수 있는 최대 던전 수 리턴.
    n = len(data)
    res = 0
    temp = list(range(n))
    
    for e in itertools.permutations(temp, n):
        #e에 저장된 인덱스 순서로 탐험할 때...
        for i in range(n):
            p = k
            cnt = 0
            for idx in e:
                a,b = data[idx][0], data[idx][1]
                if p >= a:
                    p -= b
                    cnt += 1
            res = max(res, cnt)
    return res
