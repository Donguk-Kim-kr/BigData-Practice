# 1.
# univ = input('학교 : ')
# dept = input('학과 : ')
# name = input('이름 : ')
# phone = input('연락처 : ')
# print()
# print(f'{name} 학생은 {univ} {dept}에 재학 중이며, 연락처는 {phone} 입니다.')

# 2.
# name = input('이름 : ')
# year = int(input('출생년도 : '))
# age = 2023 - year + 1
# print(f'2023년 기준, {name} 님의 한국 나이는 {age}세 입니다.')

# 3.
# month = int(input('오늘은 몇 월입니까? : '))
# if 3 <= month <= 5 :
#     print('봄!')
# elif 6 <= month <= 8 :
#     print('여름!')
# elif 9 <= month <= 11 :
#     print('가을!')
# elif month == 12 or 1 <= month <= 2 :
#     print('겨울!')
# else :
#     print('1 ~ 12 사이의 숫자를 입력해주세요.')

# 4.
# score1 = int(input('1차 점수 입력 : '))
# score2 = int(input('2차 점수 입력 : '))
# avg = (score1 + score2) / 2 # 평균
# if score1 >= 50 and score2 >= 50 and avg >= 70:
#     print('합격')
# else:
#     print('불합격')

# 5.
# 라이브러리 불러오기
# import 불러올 라이브러리명
# 그 안의 함수 호출(실행)
# --> 라이브러리명.함수명()

# import random
# com = random.randint(1, 30) # 1 ~ 30 중 하나의 정수 추출
# print('1 ~ 30 숫자 맞히기 게임')
# while True:
#     player = int(input('숫자 입력(종료 0) : '))
#     if player == 0:
#         break
#     elif player == com:
#         print('정답입니다.')
#         break
#     elif player > com:
#         print('다운!')
#     else:
#         print('업!')

# 6.
# import random

# lotto = [] # 빈 리스트
# while True:
#     num = random.randint(1, 45) # 1 ~ 45 중에서 하나 추출
#     if num not in lotto: #중복이 없으면
#         lotto.append(num)
#     if len(lotto) == 6:
#         break
# lotto.sort()
# print(lotto)

# print()

# # random.sample(범위, 개수) --> 범위에서 개수만큼 중복되지 않은 수를 추출
# lotto2 = random.sample(range(1, 46), 6)
# lotto.sort()
# print(lotto2)

# 7.

# import random
# word = ["함수", "미분", "적분", "행렬", "벡터", "확률", "명제", "방정식", "로그", "집합"]
# input('타자게임 시작(엔터 입력)')

# n = 1 # 문제 번호
# w = random.choice(word)
# while True:
#     w = random.choice(word)
#     my = input(f'문제 {n} (종료 0) : {w}\n')
#     if my == '0':
#         break # 0을 입력하면 종료!
#     elif my == w:
#         print('정답!')
#         w = random.choice(word)
#     else:
#         print('오답!')
#     n += 1

# 8.
# vote = {'대성리' : 0, '춘천' : 0, '을왕리' : 0, '청평' : 0}
# print('<<MT 장소 투표>>')
# for key in vote:
#     print(f'{key}:{vote[key]}표', end = ' ')
# print('\n')
# for i in range(1, 5):
#     pick = input('장소: ')
#     vote[pick] += 1

# print('장소 :')
# for key in vote:    
#     print(f'{key}:{vote[key]}표', end = ' ')
# print()
# winner = max(vote, key=vote.get)
# print(f"최다득표 : {winner} {vote[winner]}표")

# vote = {'대성리' : 0, '춘천' : 0, '을왕리' : 0, '청평' : 0}
# print('<<MT 장소 투표>>')
# for key in vote:
#     print(f'{key}:{vote[key]}표', end = ' ')
# print('\n')

# while True:
#     area = input('장소 : ')
#     if not area:
#         break
#     vote[area] = vote[area] + 1

# for key in vote:
#     print(f'{key}:{vote[key]}표', end = ' ')
# print('\n')

# max(값들) : 최대값
# min(값들) : 최소값
# max_key = max(vote, key=vote.get)
# print(f'최다득표 : {max_key}:{vote[max_key]}표')

# 10.
# def price(menue):
#     if menue == 1:
#         m = '아메리카노'
#         p = 3000
#     elif menue == 2:
#         m = '카페라떼'
#         p = 4000
#     elif menue == 3:
#         m = '바닐라라떼'
#         p = 4500
#     print(f'{m}: {p:,}원') # 천단위 구분 기호 추가

# menue = int(input('메뉴선택(1:아메리카노/2:카페라떼/3:바닐라라떼) '))
# price(menue)

# 11.
files = ['report.hwp', 'newjeans', 'attention.png', 'ditto.jpg', 'address.xslx']

result = filter(lambda x: 'jpg' in x or 'png' in x, files)
print(list(result))