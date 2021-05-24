from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from services.ProductService import ProductService
from services.CategoryService import CategoryService

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
