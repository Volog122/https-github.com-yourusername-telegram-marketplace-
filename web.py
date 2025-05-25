from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/items")
def get_items():
    # Пример данных (можно заменить на чтение из БД)
    items = [
        {"id": 1, "title": "AI Бот", "price": 100, "category": "bot"},
        {"id": 2, "title": "Мем-чат", "price": 50, "category": "chat"},
    ]
    return jsonify(items)


if __name__ == "__main__":
    port = int(
        os.environ.get("PORT", 5000)
    )  # Использует PORT от Render или 5000 локально
    app.run(host="0.0.0.0", port=port)  # Слушает правильный порт
