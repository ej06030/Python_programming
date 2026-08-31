# 불리언(bool)

a = True
print(a, type(a))

print(2 < 3) # True
print(2 > 3) # False
print(2 == 3) # False
print(2 != 3) # True

print("apple" < "banana") # 문자열은 사전식으로 비교, 출력값: True

# bool()
print(bool(3)) # True
print(bool(0)) # False
print(bool("Hello")) # True
print(bool("")) # False
print(bool([10])) # True
print(bool([])) # False

# None 자료형
a = None
print(a, type(a)) 
print(bool(a)) # False

#ex)
if a is None:
    print("값이 없습니다.")
