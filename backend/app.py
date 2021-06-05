from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from services.ProductService import ProductService
from services.CategoryService import CategoryService
from services.OrderService import OrderService

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/menu/category', methods=['GET'])
@cross_origin()
def get_categories():
    """Returns in a json all categories"""
    category_service = CategoryService()
    return jsonify(category_service.get_categories())


@app.route('/menu/product', methods=['GET'])
@cross_origin()
def get_products():
    """Returns in a json all products"""
    product_service = ProductService()
    return jsonify(product_service.get_products())


@app.route('/order', methods=['POST'])
@cross_origin()
def create_order():
    """Create an order on the system"""
    payment_info = request.json["orderInfo"]

    order_service = OrderService()
    created, errors = order_service.create_order(payment_info)

    status_code = 201 if created else 400

    return errors, status_code


@app.route('/order', methods=['GET'])
@cross_origin()
def get_orders():
    """Get all orders made"""
    order_service = OrderService()
    return jsonify(order_service.get_orders())
