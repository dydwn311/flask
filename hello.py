from flask import Flask, escape, request, render_template
import random
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


@app.route('/variable')
def variable():
    name ="해피해킹"
    return render_template('variable.html',html_name=name)

@app.route('/greeting/<string:name>')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name = def_name)

@app.route('/cube/<int:num>')
def cube(num):
    cube_num = num**3
    return render_template('cube.html',num =num, cube_num = cube_num)

@app.route('/lunch')
def lunch():
    # menu 리스트를 만들어주세요.
    menu = ['치킨집', '양자강','감자탕']

    #dic으로 작성하기
    menus = {
        "양자강" :"https://steemitimages.com/DQmNPAY4m1GVTVcmer7qmLkrUJ5G1eMeSPVefSbsUXKWQAD/20180403_114159.jpg",
        "치킨집" : "https://www.mpps.co.kr/kfcs_api_img/KFCS/goods/DL_2172965_20181218164144426.png",
        "감자탕" : "http://ebadom.com/upload/menu_01/2017_07_06/hero_uRpFU_2017_07_06_12_09_50.jpg"
    }

    menu_list = list(menus.keys())
    pick = random.choice(menu_list)
    img =menus[pick]
    
    


    choicesrc= ""
    choice = random.choice(menu)
    if choice == '치킨집':
        choicesrc= "https://www.mpps.co.kr/kfcs_api_img/KFCS/goods/DL_2172965_20181218164144426.png"
    elif choice == '양자강':
        choicesrc= "https://steemitimages.com/DQmNPAY4m1GVTVcmer7qmLkrUJ5G1eMeSPVefSbsUXKWQAD/20180403_114159.jpg"
    elif choice =='감자탕':
        choicesrc= "http://ebadom.com/upload/menu_01/2017_07_06/hero_uRpFU_2017_07_06_12_09_50.jpg"

   

    # return render_template('lunch.html',lunch_name=choice,lunch_image=choicesrc )
    return render_template('lunch.html',lunch_name=pick,lunch_image=img )


@app.route('/movies')
def movies():
    movies = ['겨울왕국2', '쥬만지', '포드v페라리']

    return render_template('movies.html',movies =movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong', methods = ['GET', 'POST'])
def pong():
    #print(request.form.get('keyword'))
    
    #get방식 html파일에서도 method 바꿔줘야한다.
    #keyword =request.args.get('keyword')


    #post방식
    keyword =request.form.get('keyword')
    return render_template('pong.html', keyword=keyword)
   

@app.route('/naver')
def naver():
    
    return render_template('naver.html')

@app.route('/google')
def google():
    
    return render_template('google.html')


#url에 데이터가 뜨면 get방식 아니면 post 방식이다
if __name__=='__main__':
    app.run(debug=True) #이걸로 인해 개발자 모드로 서버를 킬 필요가없음


#get방식 : 서버야 나 이것좀 줘

#post방식 : 서버야 나 이것좀 처리해줘 / post는 form방식으로 보통 