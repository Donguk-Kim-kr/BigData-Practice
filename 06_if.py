# 회원이면 '어서오세요'라는 인사말 출력
# member = input('회원입니까? : (y/n)')
# if member == 'y':
#     print('어서오세요 회원님')
# elif member == 'n':
#     newmember = input('회원 가입 하시겠습니까? : (y/n)')
#     print(newmember)
#     if newmember == 'y':
#         print('어서오세요 회원님')
#     elif newmember == 'n':
#         print('환영합니다 비회원님')
#     else:
#         print('잘못 누르셨습니다')
# else:
#     print('잘못 누르셨습니다')

age = int(input('나이를 입력해주세요 : '))
price = 20000
if age < 6:
    print(f'입장료는 무료입니다.')
elif age < 60:
    print(f'입장료는 {price}원 입니다.')
elif age < 120:
    print(f'입장료는 {price // 2}원 입니다.')
else:
    print(f'잘못 입력하셨습니다. 이용을 종료합니다.')