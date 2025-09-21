import sys
from collections import Counter

# 두 문자열 차이.
# 두 문자열의 길이가 같아질 때까지 연산 가능
# A의 앞에 아무 알파벳 추가, A의 뒤에 아무 알파벳이나 추가
# 이때 A와 B의 길이가 같으면서 A와 B의 차이를 최소로.
# A를 B의 각 위치에 맞춰서 최소값을 찾아야 함.

strA, strB = map(str, input().split())
res = int(1e9)
for i in range(len(strB) - len(strA) + 1):
    diff = 0
    for j in range(len(strA)):
        if strA[j] != strB[i+j]:
            diff += 1
    res = min(res, diff)

print(res)