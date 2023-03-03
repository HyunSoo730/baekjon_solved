def solution(number, k):
    n = len(number)
    res = []
    
    data = number
    for idx, x in enumerate(data):
        if len(res) == 0: #비어있다면
            res.append(x)
            continue
        if k>0: #아직 제거 가능
            while res[-1] < x: #스택 마지막 수가 현재 수보다 작으면. 꺼내야지
                res.pop() #제거했으니
                k -= 1 #제거 가능 횟수 줄여야함.
                if len(res) == 0 or k == 0: #비었거나 다 지웠으면 탈출
                    break
        res.append(x)
        #즉 현재 숫자 x에 대해서 스택 안에 저장한 값과 계속 비교를 하는 것이다.ㅔ갸
        
    while k > 0: #아직 남았을 수도 있어서
        res.pop()
        k -= 1 
    temp = ""
    for x in res:
        temp += x
    return temp
        
        
