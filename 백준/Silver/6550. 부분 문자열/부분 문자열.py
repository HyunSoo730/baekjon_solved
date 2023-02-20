import sys

from collections import deque

#s가 t의 부분문자열인지 판단
while True:
    try:
        s,t = input().split()
        flag = 0
        idx = 0
        for i in range(len(t)):
            if t[i] == s[idx]:
                idx += 1
                if idx == len(s): #모든 문자 발견
                    flag = 1
                    break
        if flag == 1:
            print("Yes")
        else:
            print("No")
    except:
        break

    