from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    logging.info(f"Received data: {data}")  # Логирование полученных данных

    if not data:
        logging.warning("No JSON data received")  # Логирование предупреждения
        return jsonify({'status': 'error', 'message': 'Invalid JSON'}), 415

    transaction_status = data.get('transactionStatus')
    logging.info(f"Transaction status: {transaction_status}")  # Логирование статуса транзакции

    if transaction_status == 'Approved':
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'error'}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
