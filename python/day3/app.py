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

    #번역
    C_ID = config('C_ID')
    C_SC = config('C_SC')
    url = 'https://openapi.naver.com/v1/papago/n2mt'

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        'X-Naver-Client-Id': C_ID,
        'X-Naver-Client-Secret': C_SC
    }


    if '/번역' in text:
        
        re_txt = text.replace("/번역", "")
        data = {
        "source": "ko",
        "target": "en",
        "text": re_txt
        }
        res = requests.post(url, headers=headers, data=data).json()
        print(res)
        msg = res.get('message').get('result').get('translatedText')
        send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={msg}').json()




    if text == '로또' :
        send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={RandomNum}').json()

    # else :
    #     send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={req}').json()
    


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