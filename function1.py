# function1
# 함수 정의
def setValue(newValue):
    x = newValue
    print("지역변수:", x)

# 함수 호출
result = setValue(5)
print(result)

# 함수 정의
def swap(x,y):
    return y, x

# 호출
print(swap(3,4))

# 교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    # 지역변수
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print(intersect("HAM", "SPAM"))
