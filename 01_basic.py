# 주석
# 변수 만들기
# <형식>
# 변수명 = 값
# hello = '안녕 파이썬' # 작은 따옴표, 큰 따옴표 모두 사용 가능.
# print(hello)

# hello5 = 'aaa'
# 5hello = 'aaa' # 숫자로 시작할 수 없다.
# import = 'a' # 예약어도 명령어로 사용할 수 없다.

# ctrl + / --> 한번에 주석 처리 및 해제

# 예약어 확인
# import keyword
# print(keyword.kwlist)

# print() # 빈 줄

# 본인의 이름과 나이를 변수에 저장한 후 출력 (67쪽 예제)
# name = '보드게이머'
# age = 18
# print(name, age)
# print(name, age, sep = '::')

# print()

# 자료형
# 기본 자료형 : int(정수형), float(실수), bool(논리, 불), str(문자열)
# 컬렉션 자료형 : list(리스트), dict(딕셔너리), tuple(튜플), set(세트)
num = 100
print(num)
print(type(num)) # 자료의 타입을 볼 수 있다.

num = 95.5
print(num)
print(type(num)) # 자료의 타입을 볼 수 있다.

name = '홍길동'
print(name)
print(type(name))

result = True # True --> 참, False --> 거짓
print(result)
print(type(result))

