from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint
import random
app = Flask(__name__)

token = config('TOKEN')
base_url = f"https://api.telegram.org/bot{token}"

@app.route('/telegram')
def telegram():

    res = requests.get(f'{base_url}/getUpdates').json()
    RandomNum = random.sample(range(1,47),6)
    chat_id = res['result'][0]['message']['chat']['id']


    send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={RandomNum}').json()
    print(chat_id)
    print(send_msg)
    return ''



@app.route('/chat')
def chat():
    return render_template('chat.html')

# @app.route('/send_msg')
# def send_message():
#     req = request.args.get("chat")
    

#     res = requests.get(f'{base_url}/getUpdates').json()
#     chat_id = res['result'][0]['message']['chat']['id']

#         send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={req}').json()
    
#     return "보내기 완료"

#POST방식으로 받기
@app.route('/', methods=['POST'])
def tel_web():
    req = request.get_json().get('message')
    


    pprint(req)
    print(req['text'],req['chat']['id'])

    if req is not None:
        chat_id = req.get('chat').get('id')
        text = req.get('text')

    print(chat_id, text)


    RandomNum = random.sample(range(1,47),6)

    # year = text[6:7]
    # month = text[8:10]
    # day = text[11:13]


    # year_arr = ['시끄러운, 말 많은', '푸른', '어두운', '조용한', '웅크린', '백색', '지혜로운', '용감한', '날카로운', '욕심 많은']
    # month_arr = ['늑대','태양','양','매','황소','불꽃','나무','달빛','말','돼지','하늘','바람']
    # day_arr  = ["의 환생","의 죽음","아래에서","를(을) 보라","이(가) 노래하다","그림자","의 일격","에게 쫒기는 남자","의 행진 ","의 왕","의 유령","을 죽인자","는(은) 맨날 잠잔다","처럼","의 고향","의 전사","은(는) 나의친구","의 노래","의 정령","의 파수꾼","의 악마","와(과) 같은 사나이","를(을) 쓰러트린자","의 혼 ","은(는) 말이 없다"]

    # name= year_arr[int(year)-1] + month_arr[int(month)-1] + day_arr[int(day)-1]

    # if text in '생일' :
    #     send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={name}').json()


    if text == '로또' :
        send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={RandomNum}').json()

    else :
        send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={req}').json()
    


    return '', 200


@app.route('/papago')
def papago():
    C_ID = config('C_ID')
    C_SC = config('C_SC')
    url = 'https://openapi.naver.com/v1/papago/n2mt'

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'X-Naver-Client-Id': C_ID,
        'X-Naver-Client-Secret': C_SC
    }

    data = {
        "source": "ko",
        "target": "en",
        "text": "안녕하세요."
    }

    req = requests.post(url, headers=headers, data=data).json()
    print(req)

    return "Finish"


if __name__ =="__main__":
    app.run(debug=True)