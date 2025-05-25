from flask import Flask, render_template, jsonify, request
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
        "subscribers": 5000,
    },
    {
        "id": 2,
        "title": "Мем-чат",
        "description": "Самые смешные мемы",
        "price": 50,
        "category": "chat",
        "subscribers": 12000,
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


@app.route("/create")
def create_page():
    return render_template("create.html")


@app.route("/my_ads")
def my_ads():
    return render_template("my_ads.html")


@app.route("/api/items", methods=["GET", "POST"])
def handle_items():
    global items
    if request.method == "POST":
        item = request.json
        item["id"] = len(items) + 1
        items.append(item)
        return jsonify({"status": "ok", "item": item})

    # Фильтр по категории
    category = request.args.get("category")
    filtered = [i for i in items if not category or i.get("category") == category]
    return jsonify({"items": filtered})
