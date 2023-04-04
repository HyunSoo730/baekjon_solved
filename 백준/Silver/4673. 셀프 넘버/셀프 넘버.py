import sys

nums = list(range(1,10001))
remove_list = [] #생성자 리스트
for num in nums:
    for x in str(num):
        num += int(x)
    if num <= 10000:
        remove_list.append(num)

remove_list = set(remove_list)
for num in remove_list:
    nums.remove(num)

for x in nums:
    print(x)


