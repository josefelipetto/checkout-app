import json
from flask import Flask, jsonify, request
from services.ProductService import ProductService
from services.CategoryService import CategoryService

app = Flask(__name__)


@app.route('/menu/category', methods=['GET'])
def get_categories():
    category_service = CategoryService()
    return jsonify(category_service.get_categories())


@app.route('/menu/product', methods=['GET'])
def get_products():
    product_service = ProductService()
    return jsonify(product_service.get_products())
