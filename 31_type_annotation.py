# 타입 어노테이션(annotation)
# --> 파이썬은 자료형 선언없이 변수나 함수를 자유롭게 사용할 수 있는 특징이 있다.
# --> 자료형을 파악하기 어려운 경우가 종종 발생한다.
# --> 파이썬 3.5버전 이상에서 사용 가능
# --> 강제성이 없는 자료형에 관한 힌트를 알려준다. --> 꼭 지킬 필요가 없다.
# --> 코드 자체에도 영향을 미치지 않는다 --> 에러가 나지 않는다.

# ex) 지금까지 일반적으로 공부한 파이썬 변수 선언 방법
num = 1 # 정수 값을 담은 변수
li = [1, 2, 3, 4]
d = {"이름":"채치수", "번호":4}
print(num, li, d, sep="\n")


print(type(num), type(li), type(d), sep="\n")

# ex) 어노테이션을 넣은 변수 선언 방법
num: int = 1 # 변수 이름 : num, 변수 값은 가능하면 int형으로 해라.
li: list = [1, 2, 3, 4]
d: dict = {"이름":"채치수", "번호":4}

print(num, li, d, sep="\n")


print(type(num), type(li), type(d), sep="\n")

# 함수

# ex) 일반적인 함수 정의 방법
def A(a, b):
    return a + b

# ex) 어노테이션을 넣은 함수 정의 방법
# def 함수명(매개변수: 자료형) -> 반환형의 자료형:
#     함수 본체
def B(a: int, b: int) -> int:
    return a + b

a1 = A(2, 3) # 정수
a2 = A(2.3, 5.7) # 실수
a3 = A("피카", "츄") # 문자열
a4 = A(["피", "카", "츄"], ["라", "이", "츄"])
b = B(4, 0.1)

print(a1)
print(a2)
print(a3)
print(a4)
print(b)
print(type(b))