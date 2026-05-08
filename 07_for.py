# for와 문자열
hello = '안녕하세요!'
for h in hello:
    print(h, end = '')
print()

# for와 리스트
li = ['sin', 'cos', 'tan', 'sec', 'cosec', 'cot']
for i in li:
    print(i, end = ', ')
print()

# for와 딕셔너리
menu = {'김밥':3000, '라면':5000, '순대':2000, '만두':2000, '떡볶이':4000}
for m in menu:
    print(m) # key가 출력됩니다.

for m in menu:
    print(menu[m]) # key(m)에 해당하는 값이 출력

for k, v in menu.items():
    print(f'key:{k}, value:{v}')

for dic in menu.items():
    print(dic)

for m in menu:
    print(f'{m} : {menu[m]}')

for i in range(30):
    print(i + 1, end = ', ')

print()

for i in range(30,0,-1):
    print(i, end = ', ')