import requests
from decouple import config
from pprint import pprint


token = config('TOKEN')
base_url = f"https://api.telegram.org/bot{token}"
url = 'xc7230.pythonanywhere.com'
setweb_url = f'/setWebhook?url={url}'

req = requests.get(base_url + setweb_url).json()

pprint(req)
