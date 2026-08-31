# 변수
a = 1
b = 3

print(a, b)

a, b = 2, 3


temp = a
a = b
b = temp
print(a, b)

a, b = b, a

# 변수명 규칙(C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 금지
# 예약어 사용 금지
# 대소문자 구분

# name! = "뽀로로" (X)
# 2name = "뽀로로" (X)

studentName = "뽀로로"
student_name = "뽀로로"

MAX_SCORe = 100
