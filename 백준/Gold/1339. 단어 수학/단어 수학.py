import heapq
import sys
from collections import defaultdict, deque


# 단어 수학.
# n개의 단어, 각 단어 알파벳 대문자.
# 각 문자를 0~9 중 하나로 바꿔서 N개의 수를 합하는 문제.같은 알파벳은 같은 숫자로 바꿔야 함,같은 숫자 겹치면 안됨
# N개의 단어 -> 그 수의 합 최대

n = int(input())
data = []
map = defaultdict(int)
for _ in range(n):
    words = input() # 단어 입력
    data.append(words)
    for i in range(len(words)):
        now = words[i]
        map[now] += 10 ** (len(words) - i - 1)

# 값이 큰 순서대로 큰 값 부여 : value 기준
map = dict(sorted(map.items(), key = lambda x : x[1], reverse = True)) # value를 기준으로 내림차순 정렬
num_dict = defaultdict(int)
num = 9
for key, val in map.items():
    num_dict[key] = num
    num -= 1

# print(num_dict.items())
# print(data)
res = 0
for words in data:
    now = ""
    for word in words:
        now += str(num_dict[word])
    # print(now)
    res += int(now)
print(res)