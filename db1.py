# db1.py
import sqlite3

# 연결 객체 생성
con = sqlite3.connect(":memory:")

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

# 검색 구문
cur.execute("SELECT * FROM PHONEBOOK;")

for row in cur:
    print(row)