# sqlite3 라이브러리 import
import sqlite3

# 'guestbook.db' 데이터베이스 파일 생성/연결
conn = sqlite3.connect('guestbook.db')

# 데이터베이스 커서 활성화(조작 준비)
cur = conn.cursor()

# 'guestball' 이라는 이름의 테이블이 존재하지 않다면 만들기 
# id는 글 번호(순서), name은 이름, msg는 메시지를 저장할 공간
cur.execute('''
CREATE TABLE IF NOT EXISTS guestbook (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    msg TEXT NOT NULL
)
''')

# 모든 변경사항을 데이터베이스 파일에 저장
conn.commit()

# 데이터베이스 연결 종료
conn.close()

# 터미널에 메시지 출력
print("데이터베이스와 테이블이 성공적으로 준비되었습니다.")