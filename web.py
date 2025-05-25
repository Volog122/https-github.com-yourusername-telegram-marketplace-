from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/items")
def get_items():
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
