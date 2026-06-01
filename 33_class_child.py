# 상속
# --> 부모(슈퍼) 클래스의 코드를 자석(서브) 크래스가 물려받는다.

class Animal :
    def _init__(self):
        self.height = 30

    def get_height(self):
        print(f"동물 {self.height}")

fubao = Animal()
fubao.get_height()

class Dog(Animal):
    mung.get_height()

    