from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/items")
def get_items():
    category = request.args.get("category")

    items = [
        {"id": 1, "title": "AI Бот", "price": 100, "category": "bot"},
        {"id": 2, "title": "Мем-чат", "price": 50, "category": "chat"},
        {"id": 3, "title": "TON NFT", "price": 70, "category": "nft"},
        {"id": 4, "title": ".ton домен", "price": 1.5, "category": "ton"},
    ]

    if category:
        filtered = [item for item in items if item["category"] == category]
        return jsonify({"items": filtered})

    return jsonify({"items": items})
