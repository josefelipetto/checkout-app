import sqlite3
from typing import List


# Responsible for holding all category business logic
class ProductService:

    def __init__(self):
        """Setup database connection and other properties"""
        self.connection = sqlite3.connect('/data/checkoutapp.db')
        self.connection.row_factory = sqlite3.Row
        pass

    def get_products(self) -> List:
        """Returns a list of products"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT category_id, id, image_id, name, price FROM Products")
        return [dict(row) for row in cursor.fetchall()]
