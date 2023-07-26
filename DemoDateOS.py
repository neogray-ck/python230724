# DemoDateOS.py
from datetime import * # datetime의 method를 모듈 언급 없이 사용하기 위함

print(dir()) # method 리스트 확인

d1 = date(2023, 7, 20)
print(d1)

d2 = date.today()
print(d2)

d3 = timedelta(days=100)
print(f"100일을 더하면:{d3}") # 텍스트 앞의 f는?? .format()을 이용한 구문을 축약
print("100일을 더하면:{0}".format(d3))
d4 = datetime.now()
print(d4)

import random
print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)]) # print문의 [...] 는 list comprehension
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 5)) # sample 함수를 쓰면 중복되지 않은 값을 도출
print(random.sample(range(20), 5))

from os.path import *
print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))
print(getsize("c:\\python310\\python.exe"))

if isfile("c:\\python310\\python.exe"):
    print("File is existed.")
else:
    print("File is not existed")

lotto = list(range(1, 46))
random.shuffle(lotto)
print(lotto)

from os import *

print("OS Name :", name)
print("Environment Variables :", environ)
#print(system("notepad.exe"))

print("Current dir.:", getcwd())
chdir("..")
print("Current dir.:", getcwd())
chdir("c:\\work")

import glob
result = glob.glob("*.py")
print(result)

for item in result:
    print(item)

#for item in glob.iglob("*.*"):
#    print(item)