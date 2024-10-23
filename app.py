from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)  # Для отладки, чтобы увидеть входящие данные
    return jsonify({"status": "success"}), 200
