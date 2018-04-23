from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Ifat's RESTful API"

@app.route("/product")
def product():
    productList = [
        {
            'name': 'Bubi Antibody',
            'rating': 5
        }
    ]
    return jsonify(productList)

if __name__ == "__main__":
    app.run()