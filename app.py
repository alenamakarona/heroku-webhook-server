from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data['transactionStatus'] == 'Approved':
        # Обработка успешной оплаты
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})

if __name__ == '__main__':
    # Указываем, что приложение будет слушать указанный порт
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
