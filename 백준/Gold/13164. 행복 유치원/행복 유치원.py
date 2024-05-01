import sys


# n명의 원생들을 키 순서대로 일렬로 줄 세우고, 총 k개의 조로 나누기
# 각 조에는 원생이 적어도 한명 필요, 같은 조에 속한 원생들은 서로 인접해 있어야 한다.
# 티셔츠 비용 = 가장 키 큰 원생 - 가장 키 작은 원생 차이
# 비용 최소화 -> k개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하기

n,k = map(int, input().split()) # 원생 수, 조 수
data= list(map(int, input().split()))
data.sort()
# print(data)
diff = [0] * (n-1)
for i in range(1,n):
    diff[i-1] = data[i] - data[i-1]
diff.sort(reverse = True)
# print(diff)
# k-1개의 막대기로 그룹을 나눠야함. 그럼 막대기는 어디에 두어야 하는가 ?
# 차이가 가장 큰 곳에 k-1개를 두어야 함.

# 일반화
# 1. 인접한 원생들 사이 키차이 구하기
# 2. 키차이 내림차순 정렬
# 막대기 k-1개를 조로 나눈다. 즉 내림차순으로 정렬된 수열에서 k-1개 제외

print(sum(diff[k-1:]))