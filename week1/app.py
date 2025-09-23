# flask 라이브러리에서 모듈 import
from flask import Flask, request, render_template
# sqlite3 라이브러리 import (데이터베이스)
import sqlite3

# Flask 앱 생성
app = Flask(__name__)

# 메인 페이지('/')에 접속했을 때 실행
@app.route('/')
def home():
    # 'guestbook.db' 파일(데이터베이스) 생성/연결
    conn = sqlite3.connect('guestbook.db')
    # 데이터베이스 커서 활성화(조작 준비)
    cur = conn.cursor()
    # guestbook에서 id, name, msg 데이터를 id 내림차순으로 정렬
    cur.execute("SELECT id, name, msg FROM guestbook ORDER BY id DESC")
    # 위에서 선택한 모든 데이터를 가져와서 entries 변수에 저장
    dataa = cur.fetchall()
    # 데이터베이스 연결 닫기
    conn.close()
    
    # index.html 파일을 화면에 띄움. 방명록 데이터(entries)를 함께 전달
    return render_template('index.html', guestbook_entries=dataa)

# '/search'로 접속했을 때 실행하는 함수
@app.route('/search')
def search():
    # URL 주소에서 'q' 라는 이름의 값을 가쟈오기. 없으면 빈칸 처리
    query = request.args.get('q', '')
    # 검색 결과를 보여줄 문장 생성
    result_text = f"'{query}'에 대한 검색 결과입니다."
    
    # 방명록은 계속 보이도록 방명록 데이터를 가져오기
    conn = sqlite3.connect('guestbook.db')
    cur = conn.cursor()
    cur.execute("SELECT id, name, msg FROM guestbook ORDER BY id DESC")
    entries = cur.fetchall()
    conn.close()
    
    # 검색 결과와 방명록 데이터 모두 전달
    return render_template('index.html', search_result=result_text, guestbook_entries=entries)

# '/write'로 접속했을 때 실행하는 함수
@app.route('/write')
def write():
    # URL 주소에서 'name'값을 가져오기
    name = request.args.get('name', '')
    # URL 주소에서 'msg'값을 가져오기
    msg = request.args.get('msg', '')

    # name과 msg가 둘 다 값이 있을 때 실행
    if name and msg:
        # 데이터베이스 연결
        conn = sqlite3.connect('guestbook.db')
        cur = conn.cursor()
        # guestbook에 새로운 데이터를 추가. (name, msg) 위치에 (?, ?)(플레이스홀더) 값을 넣기
        cur.execute("INSERT INTO guestbook (name, msg) VALUES (?, ?)", (name, msg))
        # 변경된 내용을 데이터베이스에 저장
        conn.commit()
        # 데이터베이스 연결 닫기
        conn.close()

    # home() 함수를 다시 실행, 최신 방명록 목록을 불러오기
    return home()

# 파이썬 파일을 직접 실행했을 때만 아래 코드 실행.
if __name__ == '__main__':
    # Flask 웹 서버를 실행 (코드 수정 시 서버는 자동 재시작)
    app.run(debug=True)