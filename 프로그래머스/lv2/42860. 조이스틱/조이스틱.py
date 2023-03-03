from collections import deque
def solution(name):
    res = 0
    
    #기본 최소 좌우 이동은 길이 -1
    min_move = len(name) -1
    
    for idx, word in enumerate(name):
        caseA = ord(word) - ord("A")
        caseB = ord("Z") - ord(word) + 1#(A->Z가는거 1)
        res += min(caseA, caseB)
        
        #해당 알파벳 다음부터 연속된 A문자열 찾기
        next = idx+1 #다음 문자열부터...
        while next < len(name) and name[next] == "A":
            next += 1
        #next가 연속된 A를 건너뛰고 나오는 인덱스
        
        #기존 움직임, 연속된 A의 왼쪽 시작방식, 연속된 A의 오른쪽 시작방식 비교해서 갱신하기
        #연속된 A의 왼쪽 시작 방식
        tempA = 2*idx + len(name) - next #왔던 길이라 *2
        tempB = idx + 2*(len(name) - next)
        min_move = min(min_move, tempA, tempB)
    res += min_move
    print(res)
    return res
        
        
    