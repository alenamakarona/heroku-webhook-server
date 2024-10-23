@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Получение данных из запроса
    # Обработка данных
    print(data)  # Для отладки, чтобы увидеть входящие данные
    return jsonify({"status": "success"}), 200
