# 반복문 : while문, for문

# while문 
# 1 ~ 10 까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5:
        break # break로 나올 시 else 실행 안됨.
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 3
i = 0

while i < len(nums) :
    if target == nums[i] :
        print(f"{target} found. index: {i}")
        break
    i += 1
else:
    print(f"{target} not detected")

# if not found:
    # print(f"{target} not found")

# 1 ~ 10 까지의 합
# sum = 55
i = 0
tot = 0 

while i <= 10 :
    i += 1
    if i % 2 == 1:
        continue
    tot += i
print(tot)