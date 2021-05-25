from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from services.ProductService import ProductService
from services.CategoryService import CategoryService
from services.OrderService import OrderService
import sys

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/menu/category', methods=['GET'])
@cross_origin()
def get_categories():
    category_service = CategoryService()
    return jsonify(category_service.get_categories())


@app.route('/menu/product', methods=['GET'])
@cross_origin()
def get_products():
    product_service = ProductService()
    return jsonify(product_service.get_products())


@app.route('/order', methods=['POST'])
@cross_origin()
def create_order():
    payment_info = request.json["paymentInfo"]
    order_service = OrderService()
    worked, check = order_service.create_order(payment_info)
    return jsonify(check), 201

@app.route('/order', methods=['GET'])
@cross_origin()
def get_orders():
    order_service = OrderService()
    return jsonify(order_service.get_orders())
