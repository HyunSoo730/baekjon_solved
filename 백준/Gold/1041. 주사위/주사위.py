import sys

#보여지는 면의 수에 따라서 생각해야함.
N = int(input())
data =  list(map(int, input().split()))

res = 0
minList = []  #마주보는 면 중 최솟값 저장용 리스트
if N == 1:
    data.sort()
    for i in range(5):
        res += data[i]
else:  #개수 여러개로 정육면체
    minList.append(min(data[0], data[5]))
    minList.append(min(data[1], data[4]))
    minList.append(min(data[2], data[3]))

    #면이 1개, 2개, 3개 보이는 걸로 나눠서
    minList.sort()
    ss1 =minList[0]  #1면만 보여질 때 사용
    ss2 = minList[0] + minList[1]  #2면만 보여질 때 사용
    ss3 = sum(minList)     #3면만 보여질 때 사용

    #이제 각 면이 보여진 개수
    c1 = (N-2) * (N-1) * 4 + (N-2) * (N-2)
    c2 = (N-1) * 4 + (N-2) * 4
    c3 = 4

    res += ss1 * c1
    res += ss2 * c2
    res += ss3 * c3

print(res)