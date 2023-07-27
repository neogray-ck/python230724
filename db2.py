# db2.py
import sqlite3

# 연결 객체 생성
con = sqlite3.connect("c:\\work\\sample.db")

# 커서 객체
cur = con.cursor()

# 테이블 생성
cur.execute("""CREATE TABLE IF NOT EXISTS PHONEBOOK
               (
                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NAME TEXT,
                 PHONENUM TEXT
               );""")

# 데이터 1건 입력
cur.execute("""INSERT INTO PHONEBOOK(NAME, PHONENUM)
               VALUES('홍길동', '010-111');""")

# 입력 파라미터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("INSERT INTO PHONEBOOK (NAME, PHONENUM) VALUES (?, ?);", (name, phoneNumber))

# 다중 행 입력
datalist = (("이순신", "010-333"), ("박문수", "010-123"))
cur.executemany("INSERT INTO PHONEBOOK (NAME, PHONENUM) VALUES (?, ?);", datalist)

# 검색 구문
cur.execute("SELECT * FROM PHONEBOOK;")
print(cur.fetchall())

#작업 완료
con.commit()
