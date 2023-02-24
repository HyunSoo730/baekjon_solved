from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0 #바로 끝내기
    
    n = len(words)
    ch = [0] * n
    res = 0
    def BFS():
        dq = deque()#해당 단어를 만드는데 몇번 걸렸는지를 확인하는 카운트도 함께.
        dq.append((begin, 0))
        
        while dq:
            word, cnt = dq.popleft()
            if word == target:
                return cnt
            #그게 아니라면 계속 찾아나가야함(상태트리)
            for i in range(n): #단어 개수만큼
                if ch[i] == 0: #아직 확인 안한 단어
                    temp = words[i]
                    m = len(temp)
                    count = 0
                    for j in range(m):
                        if word[j] != temp[j]:
                            count += 1
                    if count == 1: #한글자만 다른 경우 뻗어나갈 수 있음
                        dq.append((temp, cnt + 1))
                        ch[i] = 1 #넣을꺼니까 갱신
        return 0
    res = BFS()
    return res
                        
            