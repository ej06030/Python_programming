# 문자열(str)
# '', ""


a = "python"
print(a, type(a))

print("I'll be back") # print('I'll be back') -> 에러 발생, \' 이스케이프 문자로 사용   

# 여러줄 문자열

a = """
Life is short
You need python
"""

print(a)

# docsrting
def func():
    """
    fucn() 함수에 대한 설명 작성
    """
    pass

print(func.__doc__)

# 문자열 연결
print("Hello" + "Python")

# 문자열 반복
print("Hello" * 10)
print("-" * 50) 

# 문자열 연산시 주의사항
#print("Hello" + 3)

print("10" + "2")
print(int("10") + int("2"))

# 문자열 포맷팅 (f-string)
name = "뽀로로"
age = 23

print(f"이름: {name}, 나이: {age}")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789
print(f"{num : ,}") # 1,000 단위 ,

print(f"{num:15,d}")
print(f"{num:<15,d}")

print(f"{num:015,d}")
print(f"{num:<015,d}")