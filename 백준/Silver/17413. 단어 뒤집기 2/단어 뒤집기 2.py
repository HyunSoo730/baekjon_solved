import sys
from collections import deque

i = 0
start = 0
data = list(input())
while i < len(data):
    if data[i] == "<": #열린 괄호 만나면
        i += 1
        while data[i] != ">":
            i += 1
        i += 1 #닫힌괄호까지는 그냥
    elif data[i].isalnum(): #숫자나 알파벳을 만나면
        start = i
        while i < len(data) and data[i].isalnum(): #아직 다 안돌았고, 숫자나 알파벳이라면
            i += 1
        #탈출 시 띄어쓰기 혹은 괄호를 만났어
        temp = data[start:i] #숫자나 알파벳인 지점을 받아온 후
        temp.reverse()
        data[start:i] = temp   #뒤집은 부분 바꿔치기
    else: #괄호도 아니고 숫자도 아니면 공백.
        i += 1 #그냥 증가

print("".join(data))
# for x in data:
#     print(x, end = "")