import sys
import copy


n = int(input())
data = list(map(int, input().split()))
oper = list(map(int, input().split())) #연산자 +,-,*,/ 각 개수

def cal(oper, a,b):
    if oper == 0:
        return a+b
    elif oper == 1:
        return a-b
    elif oper == 2:
        return a*b
    elif oper == 3:
        if a <0:
            return (-a // b) * -1
        else:
            return a //b

resA = int(1e9) #최소
resB = -int(1e9) #최대
def DFS(L, sum):
    global resA
    global resB
    if L == n: #연산자 모두 선택. 종료조건
        if resA > sum:
            resA = sum
        if resB < sum:
            resB = sum
    else:
        for i in range(4):
            if oper[i] > 0:
                oper[i] -= 1 #현재 연산자 사용
                DFS(L+1, cal(i, sum, data[L]))
                oper[i] += 1


DFS(1, data[0])
print(resB)
print(resA)

