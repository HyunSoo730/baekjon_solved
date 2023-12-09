import sys

n = int(input())
data = list(map(int, input().split()))

ch = [0] * n
nums = [0] * n
res = 0
def dfs(L):
    global res
    if L == n:
        sum_data = 0
        for i in range(n-1):
            sum_data += abs(nums[i] - nums[i+1])
        res = max(res, sum_data)
    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                nums[L] = data[i]
                dfs(L+1)
                ch[i] = 0
dfs(0)
print(res)