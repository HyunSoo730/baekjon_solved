
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
import itertools 
import math
def solution(numbers):
    n = len(numbers)

    data = []
    for x in numbers:
        if x.isdigit():
            data.append(int(x))

    def prime_number(x):
        if x == 0 or x == 1:
            return False
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return False
        else:
            return True    
    def make_num(data): #리스트 숫자
        res = 0
        for x in data:
            res = res * 10 + x
        return res


    i = 0
    cnt = 0
    temp_set = set()
    for i in range(1,n+1):
        for res in itertools.permutations(data,i):
            temp = make_num(res)
            if temp in temp_set:
                continue
            temp_set.add(temp)
            if prime_number(temp) == True: #소수
                # print("True")
                cnt += 1

    return cnt