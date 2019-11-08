import requests
from decouple import config
from pprint import pprint


token = config('TOKEN')
base_url = f"https://api.telegram.org/bot{token}"
url = '45866a63.ngrok.io'
setweb_url = f'/setWebhook?url={url}'

req = requests.get(base_url + setweb_url).json()

pprint(req)