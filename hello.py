from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Ifat's RESTful API"

productList = [
    {
        'name': 'Bubi Antibody',
        'rating': 5
    },
    {
        'name': 'Bubi2 Antibody',
        'rating': 4
    },
    {
        'name': 'Bubi3 Antibody',
        'rating': 3
    }
]

@app.route("/product/")
@app.route("/product/<int:product_id>")
def product(product_id=None):
    if product_id:
        return jsonify(productList[product_id])
    else:
        return jsonify(productList)

if __name__ == "__main__":
    app.run()