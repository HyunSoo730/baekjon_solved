import sys

# NxN 배열 A
# 배열에 들어있는 수 A[i][j] = i*j
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 NxN이 된다.B를 오름차순 정렬했을 때 B[k] 구하기
# N 10^5 면 N^2 안됨.
# K번째 수는 무엇인가 ? (최적화) -> X이하의 수가 K개 이상인 최소 X는 ? 첫번째 !
n = int(input())
k = int(input())

left, right = 1, n*n + 1 # 극단적으로 가장 마지막 수가 될 수도 있음.
"""
1행 : 1x1, 1x2, 1x3 ... 1xN
2행 : 2x1, 2x2, 2x3 ... 2xN
3행 : 3x1, 3x2, 3x3 ... 3xN
i행 : ix1, ix2, ix3 ... ixN

-> i행에서 X이하 ? -> ixj <= X
j <= X/i j는 개수라고 생각해도 되니까.
1 2 3
2 4 6
3 6 9
-> 1 2 2 3 3 4 6 6 9
"""
def is_possible(X): # X이하의 수가 K개 이상인가 ?
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n, X // i)

    return cnt >= k

while left < right:
    mid = (left + right) // 2

    if not is_possible(mid): # X 이하의 수가 k개 이상이 불가능 ?
        left = mid + 1
    else:
        right = mid

print(left)