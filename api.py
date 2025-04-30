from flask import Flask, jsonify, request
from db import orders_db

app = Flask(__name__)


@app.route('/orders', methods=["POST"])
def get_orders():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    if "orderNumber" not in data:
        return jsonify({"error": "Missing orderNumber"}), 400