# 표준 입력 함수 - input()
#   --> 입력을 받으면 문자열로 인식

# name = input('당신의 이름은 무엇인가요? : ')
# print(name)

# a = input('숫자 1 입력 : ')
# b = input('숫자 2 입력 : ')
# print(a + b)
# print(type(a), type(b)) # <class 'str'> <class 'str'>

# # 정수형으로 입력
# a = int(input('정수 1 입력 : '))
# b = int(input('정수 2 입력 : '))
# print(a + b)

# # 실수형으로 입력
# a = float(input('실수 1 입력 : '))
# b = float(input('실수 2 입력 : '))
# print(a + b)

# f 문자열 포매팅
a = int(input('정수 1 입력 : '))
b = int(input('정수 2 입력 : '))
print(f'{a} + {b} = {a + b}')
print('{} + {} = {}'.format(a, b, a + b))