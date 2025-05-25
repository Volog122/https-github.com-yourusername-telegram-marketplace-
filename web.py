from flask import Flask, render_template, jsonify
import os
import sqlite3

app = Flask(__name__)


# Простой тестовый API для товаров
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/items")
def get_items():
    # Временные данные (заменится на чтение из БД)
    items = [
        {
            "id": 1,
            "title": "AI Чат-бот",
            "description": "Парсинг новостей и ответы",
            "price": 100,
            "category": "bot",
        },
        {
            "id": 2,
            "title": "Мем-чат",
            "description": "Самые смешные мемы",
            "price": 50,
            "category": "chat",
        },
    ]
    return jsonify(items)


if __name__ == "__main__":
    # Используем PORT из окружения или 5000 локально
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
