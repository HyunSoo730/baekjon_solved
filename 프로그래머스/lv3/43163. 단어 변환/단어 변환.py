from collections import defaultdict, deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    ch = defaultdict(int)
    for word in words:
        ch[word] = 0
    n = len(words)
    def BFS(a,b):
        dq = deque()
        dq.append((a, b)) #해당 word까지 오는데 걸린 횟수 cnt
        ch[a] = 1 #시작 지점 방문        
        while dq:
            word, cnt = dq.popleft()
            if word == target:
                return cnt
            for w in words:
                if ch[w] == 0: #방문 전
                    check = 0
                    for i in range(len(word)):
                        if word[i] != w[i]:
                            check += 1
                    if check == 1: #같지 않은게 딱 한개라면
                        #방문 가능
                        ch[w] = 1
                        dq.append((w,cnt+1))
    res = BFS(begin,0)
    print(res)
    return res
        