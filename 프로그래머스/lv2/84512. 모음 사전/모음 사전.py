from collections import deque
def solution(word):
    #해당 word가 몇번째 단어인지.
    #한 자리에 5글자 올 수 있음. 
    MAX = 781 
    cnt = 0
    data = ["A", "E", "I", "O", "U"]
    dq = deque(word)
    ch = 0
    while dq:
        x = dq.popleft()
        ch += 1
        for i in range(5):
            temp = 0
            if x == data[i]:
                cnt += i + 1 #일단 해당 자리까지 갈 수 있는 경우
                print(i+1)
                n = 5
                j = 1
                while n -ch > 0 and i > 0: #A보다는 커야 다음 인덱스 계산 가능.
                    temp += pow(5,j)
                    j += 1
                    n -= 1
                print("temp", temp)
            cnt += (i) * temp
        print("cnt", cnt)
    return cnt
                

            