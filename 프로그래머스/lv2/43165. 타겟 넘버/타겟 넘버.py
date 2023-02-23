cnt = 0
def DFS(L, sum, data, target):
    global cnt
    if L == len(data): #모두 확인. 종료조건
        if sum == target:
            cnt += 1
    else: #더하거나 빼거나
        DFS(L+1, sum + data[L], data,target) #더하기
        DFS(L+1, sum - data[L], data,target) #빼기
        

def solution(numbers, target):
    DFS(0,0,numbers,target)
    return cnt
