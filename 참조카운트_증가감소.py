class MyClass:
    def __init__(self, value):
        self.Value = value 
        print("Instance is created! Value = ", value)
        
    def __del__(self):
        print("Instance is deleted!")
        

c = MyClass(10)
# del을 주석처리하고 실행하면
# 프로그램 종료 전에 c가 destroy되고 "Instance is deleted"가 출력된다.
# 이는 GC가 동작해서 처리한 것.
#del c
print("전체 코드 실행 종료")
