# class1.py
#1)클래스 형식 정의
class Person:
    #초기화메서드
    def __init__(self):
        #인스턴스 멤버변수
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()

#3)메서드 호출
p1.name = "전우치"
p1.print()
p2.print()

# 런타임시에 변수 추가
#  - instance에 호출된 변수가 없으면, class의 변수명을 확인
#  - class의 원형에도 해당 변수가 없으면 전역변수 확인
#  - 전역변수에서도 탐색에 실패하면 에러
#   (...이래도 되는 거 맞아??)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
