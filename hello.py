from flask import Flask, escape, request

app = Flask(__name__)
#이코드는 flask 홈페이지에서 가저온 버전
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__=='__main__':
    app.run(debug=True)

#py란 파일이 실행되는 경우 이파일 실행되거나(run) import하는 경우     