# 텔레그램봇

botfather 검색

 https://core.telegram.org/bots/api#available-methods 

https://api.telegram.org/bot/getMe 내 bot 정보
https://api.telegram.org/bot/getUpdates 내 bot 메세지 확인

https://api.telegram.org/bot/sendMessage?chat_id=?&text=안녕하세요 메세지 보내기





pip install python-decouple



## 채팅 아이디 확인

app.py

```python
from flask import Flask
import requests
from decouple import config
from pprint import pprint

app = Flask(__name__)

@app.route('/telegram')
def telegram():
    token = config('TOKEN')
    base_url = f"https://api.telegram.org/bot{token}"
    res = requests.get(f'{base_url}/getUpdates').json()

    #하위 목록 가져오기
    chat_id = res['result'][0]['message']['chat']['id']
    
    pprint(res)
    print(chat_id)
    return ''

if __name__ =="__main__":
    app.run(debug=True)
```





bot에 문자 보내기

app.py

```python
from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint
import random
app = Flask(__name__)

token = config('TOKEN')
base_url = f"https://api.telegram.org/bot{token}"

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/send_msg')
def send_message():
    req = request.args.get("chat")
    
    
    res = requests.get(f'{base_url}/getUpdates').json()
    chat_id = res['result'][0]['message']['chat']['id']

    send_msg = requests.get(f'{base_url}/sendMessage?chat_id={chat_id}&text={req}').json()

    return "보내기 완료"


if __name__ =="__main__":
    app.run(debug=True)
```

chat.html

```html
<form action="/send_msg" method="GET">
    채팅내용: <input type="text" name='chat'>
    <input type="submit" value="보내기">
</form>
```





## webhook

 https://dashboard.ngrok.com/get-started 

.ngrok.exe http

set_webhook.py



```python
import requests
from decouple import config
from pprint import pprint


token = config('TOKEN')
base_url = f"https://api.telegram.org/bot{token}"
url = '45866a63.ngrok.io'
setweb_url = f'/setWebhook?url={url}'

req = requests.get(base_url + setweb_url).json()

pprint(req)
```

