from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    name = "World!!"
    return f'Hello {name}!'


#  @app.route('/mulcam')
#  def mulcam():
#     return 'Hello mulcamp'

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'{name}님 안녕하세요'

@app.route('/lunch/<int:num>')
def lunch(num):
    menu = ["짜장면", "짬뽕", "라면", "스파게티", "스테이크", "삼겹살"]
    order = random.sample(menu, num)
    return render_template('menu.html', menu=order)

# 로또 번호
@app.route('/lotto')
def lotto():
    RandomNum = random.sample(range(1,47),6)
    return str(RandomNum)



@app.route('/html')
def html():
    multiline = '''
    <h1> This is H1 Tag </h1>
    <p> This is P Tag </p>
    '''
    return multiline


@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', name=name)



@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')



if __name__=="__main__":
    app.run(debug=True, port=8000)
