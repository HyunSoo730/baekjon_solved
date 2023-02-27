import sys

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
dp[0][0][0] = 1 #자명
def DFS(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return dp[0][0][0]
    elif a > 20 or b > 20 or c > 20:
        return DFS(20,20,20)
    
    if dp[a][b][c] > 0: #이미 값 존재
        return dp[a][b][c]
    #만약 기존 dp에 저장되어 있지 않다면 계속 해줘야함.
    
    if a<b and b<c:
        dp[a][b][c] = DFS(a,b,c-1) + DFS(a,b-1,c-1) - DFS(a,b-1,c)
    else:
        dp[a][b][c] = DFS(a-1,b,c) + DFS(a-1,b-1,c) + DFS(a-1,b,c-1) - DFS(a-1,b-1,c-1)
    
    return dp[a][b][c]
    


while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    res = DFS(a,b,c)
    print(f"w({a}, {b}, {c}) = {res}")