import sys


name = input()
alphas = [0 for _ in range(27)]  #알파벳 개수
odds = 0   #홀수 개수
oddIndex = -1 #홀수의 위치
flag = 0

for x in name:
    alphas[ord(x) -65] += 1

for i in range(len(alphas)):  #알파벳들만 이제 확인
    if alphas[i] % 2 == 1: #등장 개수가 홀수개.
        odds += 1
        oddIndex = i   #홀수의 위치는 왜??
        if odds == 2:
            flag = 1

#홀수 등장 개수가 1개 이하여야만 팰린드롬 가능

alphas[oddIndex] -= 1 #홀수의 알파벳 하나 미리 빼놓기

if flag == 0:
    for i in range(len(alphas)):
        if alphas[i] % 2 != 1:
            for _ in range(alphas[i] // 2):   #짝수개수인 것들 양쪽으로 출력할 거니깐.. 한쪽에 미리 출력
                print(chr(i + 65), end = "")

    if oddIndex != -1:  #홀수개 존재한다면
        print(chr(oddIndex + 65), end = "")

    for i in range(len(alphas) -1, -1, -1):  #우측 출력
        if alphas[i] %2 != 1:
            for _ in range(alphas[i] // 2):
                print(chr(i+65), end = "")
            
elif flag == 1:
    print("I'm Sorry Hansoo")