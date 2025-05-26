from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Тестовые данные
items = [
    {
        "id": 1,
        "title": "AI Новостной бот",
        "description": "Парсинг новостей",
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
    {
        "id": 3,
        "title": "TON NFT",
        "description": "Цифровое искусство",
        "price": 70,
        "category": "nft",
    },
    {
        "id": 4,
        "title": ".ton домен",
        "description": "Редкие .ton домены",
        "price": 1.5,
        "category": "ton",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/items")
def get_items():
    category = request.args.get("category")
    filtered = (
        items if not category else [i for i in items if i["category"] == category]
    )
    return jsonify({"items": filtered})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
