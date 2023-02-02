import sys


#대소문자 구분
data = input()
check = 0
box = ["U", "C", "P", "C"]
cnt = 0
for x in data:
    if x == box[check]:
        cnt += 1
        check += 1
    if cnt == 4:
        break

if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")