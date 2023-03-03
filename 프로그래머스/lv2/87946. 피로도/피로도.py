import itertools
def solution(k, dungeons):
    #피로도 k
    data = dungeons
    n = len(data) #던전 수
    
    res = 0
    for temp in itertools.permutations(data, n):
        #탐험 순서 temp에 저장
        p = k
        cnt = 0
        for a,b in temp:
            #a,b는 각각 최소 피로도, 소모 피로도
            if p >= a:
                p -= b
                cnt += 1
        res = max(res, cnt)
    return res
