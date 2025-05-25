from flask import Flask, render_template, jsonify
import os
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/items")
def get_items():
    try:
        with sqlite3.connect("marketplace.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM items")
            items = cur.fetchall()

        return jsonify(
            [
                {
                    "id": i[0],
                    "title": i[1],
                    "description": i[2],
                    "price": i[3],
                    "category": i[4],
                }
                for i in items
            ]
        )
    except Exception as e:
        print("Ошибка:", str(e))
        return jsonify({"error": "Не удалось загрузить товары"}), 500
