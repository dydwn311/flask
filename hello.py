from flask import Flask, escape, request, render_template

app = Flask(__name__)
#이코드는 flask 홈페이지에서 가저온 버전

#@app.route('/') :  ('/')가 들어오면 아래있는 hello()가 실행된다.
# @:데코레이터
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

#py란 파일이 실행되는 경우 이파일 실행되거나(run) import하는 경우     


@app.route('/hi')
def hi():
    return "hi"

@app.route('/change')
def change():
    return 'hello change'



@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

    
@app.route('/html_file')
def html_file():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)
