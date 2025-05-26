from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

# Тестовые данные
categories = [
    {"id": 1, "name": "Боты", "items_count": 10},
    {"id": 2, "name": "Каналы", "items_count": 5},
    {"id": 3, "name": "Сообщества", "items_count": 8},
    {"id": 4, "name": "NFT", "items_count": 3},
    {"id": 5, "name": "TON домены", "items_count": 7},
    {"id": 6, "name": "Реклама", "items_count": 2},
]

items = [
    {
        "id": 1,
        "title": "AI Новостной бот",
        "description": "Парсинг новостей",
        "price": 100,
        "ton_price": 1.5,
        "avatar": "https://via.placeholder.com/60 ",
    },
    {
        "id": 2,
        "title": "Мем-чат",
        "description": "Самые смешные мемы",
        "price": 50,
        "ton_price": null,
        "avatar": "https://via.placeholder.com/60 ",
    },
    {
        "id": 3,
        "title": "TON NFT",
        "description": "Цифровое искусство",
        "price": 70,
        "ton_price": 0.8,
        "avatar": "https://via.placeholder.com/60 ",
    },
    {
        "id": 4,
        "title": ".ton домен",
        "description": "Редкие .ton домены",
        "price": 1.5,
        "ton_price": 1.0,
        "avatar": "https://via.placeholder.com/60 ",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/categories")
def get_categories():
    return jsonify({"categories": categories})


@app.route("/api/items")
def get_items():
    category_id = request.args.get("category_id")
    if category_id:
        return jsonify({"items": [i for i in items if str(i["id"]) == category_id]})
    return jsonify({"items": items})


@app.route("/categories")
def all_categories():
    return render_template("categories.html")


@app.route("/item/<int:item_id>")
def item_detail(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        return "Товар не найден", 404
    return render_template("item_detail.html", item=item)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
