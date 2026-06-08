from csv import *

file = open("./file/library.csv", "r", encoding="cp949")
read_file = reader(file)

library_list = []
for line in read_file:
    library_list.append(line)
file.close()

library_info = ["도서관코드", "도서관이름", "주소", "상세주소", "전화번호", "팩스", "홈페이지", "개관시간", "휴무일"]

while True:
    search_word = input("검색어 입력(종료 : 0) : ")
    if search_word == "0":
        print("\n[도서관 정보 검색 시스템 종료]");break # ;넣으면 다음줄 코드
           
    print(f"\n제공 정보 --> {library_info[2:]}")

    print_info = input("\n원하는 정보 입력 (예시: 주소 휴관일)").split() # 공백을 기준으로 나눠서 저장
    print()
    print("\n[도서관 정보 검색 결과]")
    for line in library_list:
        if search_word in line[1]: # 찾는 단어가 line[1](도서관 이름)에 포함되어 있는가?
            print(line[1], end = " | ")
            for i in print_info: # 예) 휴관일
                if i in library_info:
                    print(line[library_info.index(i)], end = " | ") # 인덱스 번호를 추출 --> index()
            print()
    print()