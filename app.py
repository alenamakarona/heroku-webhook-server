from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Укажите ваш токен бота Telegram
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")  # Убедитесь, что переменная окружения установлена
WEBHOOK_URL = f'https://makarona-f5b217fb06ad.herokuapp.com/webhook'

# Установка вебхука
@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    url = f'https://api.telegram.org/bot{TOKEN}/setWebhook'
    response = requests.post(url, data={'url': WEBHOOK_URL})
    return jsonify(response.json())

# Обработка входящих обновлений
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Получение данных из запроса
    print(data)  # Для отладки, чтобы видеть входящие данные

    # Обработка сообщения
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        message_text = data['message']['text']
        
        # Пример ответа на сообщение
        send_message(chat_id, "Вы написали: " + message_text)

    return jsonify({"status": "success"}), 200

# Функция отправки сообщения
def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    requests.post(url, data={'chat_id': chat_id, 'text': text})

# Запуск приложения
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
