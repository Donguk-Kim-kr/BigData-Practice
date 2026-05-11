# 113p

# 구구단 2단
# for i in range(1, 10):
#     print(f'2 × {i} = {2 * i :2}') # 2 × 1 = 2

# 단을 입력받아 구구단 출력
# num = int(input('단 입력 : '))
# for i in range(1, 10):
#     print(f'{num} × {i} = {num * i :2}')

# 구구단 전체 출력
# 단 --> 2단 ~ 9단 --> dan
# 곱해지는 수 --> 1 ~ 9 --> i

# for dan in range(2, 10):
#     print(f'-- {dan}단 --')
#     for i in range(1, 10):    
#         print(f'{dan} × {i} = {dan * i :2}')
#     print()

# 중첩 for 이용 - 김밥 배합 출력
main = ['베이컨', '크래미']
side = ['당근', '오이']
x = 1
for m in main:
    for s in side:
        print(f'{x} : {m} + {s} + 계란')
        x += 1