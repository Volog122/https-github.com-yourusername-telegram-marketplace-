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
        "contact": "cooldev",
        "category": "bot",
        "image": "https://placehold.co/400x200?text=AI+ Бот",
        "tag": "new",
        "rating": 4,
        "reviews": 12,
    },
    {
        "id": 2,
        "title": "Мем-чат",
        "description": "Самые смешные мемы",
        "price": 50,
        "contact": "memelord",
        "category": "chat",
        "image": "https://placehold.co/400x200?text= Мем-чат",
        "tag": "",
        "rating": 4.5,
        "reviews": 30,
    },
    {
        "id": 3,
        "title": ".ton домен",
        "description": "Редкие .ton домены",
        "price": 1.5,
        "contact": "tonmaster",
        "category": "ton",
        "image": "https://placehold.co/400x200?text= @wallet.ton",
        "tag": "popular",
        "rating": 5,
        "reviews": 50,
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


@app.route("/item/<int:item_id>")
def item_detail(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        return "Товар не найден", 404
    return render_template("item_detail.html", item=item)


@app.route("/create")
def create_ad():
    return render_template("create_ad.html")


@app.route("/favorites")
def view_favorites():
    return render_template("favorites.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
