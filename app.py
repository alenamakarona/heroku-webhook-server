import requests

TOKEN = 7996920370:AAHVQPRPwGMkLQLAuaJv7DuM18QSG2T6BCg
WEBHOOK_URL = 'https://makarona-f5b217fb06ad.herokuapp.com/webhook'

def set_webhook():
    url = f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}'
    response = requests.get(url)
    return response.json()

set_webhook()
