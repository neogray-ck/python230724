# DemoRE.py
import re

#숫자가 0에서 N번th

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

# 문자열에 공백이 들어가면?
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#result = re.match("[0-9]*th", "  35th")
#print(result)
#print(result.group())


result = re.search("apple", "빅테크에서 apple의 위상")
print(result.group())
result = re.search("\d{4}", "올해는 2023년")
print(result.group())
result = re.search("\d{5}", "우리 동에는 42300")
print(result.group())

print("\n---대소문자---")
data = "Apple is big company and apple is very delicious"
c = re.compile("apple", re.IGNORECASE) # 대소문자 구분 무시
print(c.findall(data))

print("\n---다중라인검색---")
data2 = """파이썬을
배워서

누구나 사용"""
c = re.compile("^.+", re.MULTILINE) # ^:문자열의 시작, .:개행문자를 제외한 1개 문자, +:문자가 1회 이상 반복
print(c.findall(data2))
