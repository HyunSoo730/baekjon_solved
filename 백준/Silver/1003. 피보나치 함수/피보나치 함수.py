import sys


T = int(input())
#피보나치에서 0과 1 몇번 출력되는지

zero = [1,0]
one = [0,1]

def fibo(n):
    length = len(zero)
    if n >= length:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
        

for i in range(T):
    n = int(input())
    fibo(n)    
    print(zero[n], one[n])