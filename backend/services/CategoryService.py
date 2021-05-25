import sqlite3
from typing import List


# Responsible for holding all category business logic
class CategoryService:
    def __init__(self):
        """Setup database connection and other properties"""
        self.connection = sqlite3.connect('/data/checkoutapp.db')
        self.connection.row_factory = sqlite3.Row
        pass

    def get_categories(self) -> List:
        """Returns a list of categories"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name FROM Categories")
        return [dict(row) for row in cursor.fetchall()]
