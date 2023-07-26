# DemoFile.py
for i in range(0, 10):
    url = "http://www.credut.com/?page=" + str(i)
    print(url)

for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("---오른쪽 정렬---")
for x in range(1, 6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1, 6):
    print(x, "*", x, "=", str(x*x).zfill(5))

print("\n---서식 지정---")
print("{0:x} {1:b}".format(10, 10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:010.2f}".format(4/3))


#파일 쓰기
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽기
f = open("c:\\work\\demo.txt", "rt", encoding="utf-8")
result = f.read()
result = result.replace("\n", "")
print("\n---라인단위---")
f.seek(0)
print(f.readline(), end="END") # "end=" 구분은 프린트 마지막에 붙이는 내용을 명시
print(f.readline(), end="")
print("\n---리스트로 받기---")
f.seek(0)
result=f.readlines()
result[0] = result[0].strip()
print(result)

f.close()
print(result)
