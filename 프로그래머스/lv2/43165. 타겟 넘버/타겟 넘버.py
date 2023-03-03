cnt = 0
def solution(numbers, target):
    n = len(numbers)
    print(n,numbers,target)
    data = numbers
    def DFS(L, sum):
        global cnt
        if L == n: #모든 인덱스 확인, 종료조건
            if sum == target:
                cnt += 1
        else:
            DFS(L+1, sum + data[L]) #해당 인덱스 더함
            DFS(L+1, sum - data[L])
    
    DFS(0,0)
    print(cnt)
    return cnt
