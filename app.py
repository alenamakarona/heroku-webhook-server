from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data is not None and 'transactionStatus' in data:
        if data['transactionStatus'] == 'Approved':
            return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
