# while
# <형식>
# while 조건식:
#     참이면 이 코드를 수행
#     거짓이 될 때까지 반복한다.

# while True: # 터미널에서 ctrl + C 를 누르면 강제 종료(윈도우, 맥 동일)
#     print('.', end = '')

# year = 1
# while year <= 3:
#     print(f' 서당개 {year}년')
#     year += 1

# 112p
# result = None # None : 아무 것도 아니다. 없다. (예약어)
# while result != 'y':
#     print('파이썬')
#     result = input('계속하려면 입력:(종료:y)')
# print('종료합니다.')

# 캐릭터 기본 체력이 100
# 정수 데미지를 입는다. - input()
# 체력이 0이 되면 종료

# hp = 100
# while hp > 0:
#     print(f'현재 캐릭터의 체력은 {hp} 입니다.')
#     damage = int(input('얼마의 데미지를 입힐까요? : '))
#     hp -= damage
# print('캐릭터가 사망하였습니다.')

# 114p
# while True:
#     num = int(input('번호를 입력해주세요 : (종료 = 0)'))
#     if num == 0:
#         break # 반복문 강제 종료
#     print('while 무한 루프 중')

# continue --> 이번 차례는 건너뛰로 계속 진행
# 114p
# 1 ~ 30 사이의 정수 중에서 7의 배수 출력

# for x in range(1, 31):
#     if x % 7 != 0:
#         continue
#     print(f'7의 배수 : {x :2}')

