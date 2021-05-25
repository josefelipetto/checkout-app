import sqlite3
from typing import List, Dict
from flask import escape


def validate_payload(payload) -> (bool, List):
    """Validate order payload for fields existences. Returns validation result and possible list of errors"""
    errors = []
    has_errors = False
    if payload['ccCVV'] is None:
        errors.append('CVV must be present')
        has_errors = True

    if payload['ccExpiration'] is None:
        errors.append('Expiration must be present')
        has_errors = True

    if payload['ccName'] is None:
        errors.append('Name on card must be present')
        has_errors = True

    if payload['ccNumber'] is None:
        errors.append('Card number must be present')
        has_errors = True

    if payload['firstName'] is None:
        errors.append('First name must be present')
        has_errors = True

    if payload['lastName'] is None:
        errors.append('Last name must be present')
        has_errors = True

    if payload['paymentMethod'] is None:
        errors.append('Payment method must be present')
        has_errors = True

    if payload['items'] is None:
        errors.append('Items must be present')
        has_errors = True
    elif len(payload['items']) <= 0:
        errors.append('You should select some items before checking out')
        has_errors = True

    return not has_errors, errors


# Class responsible for holding all order business logic
class OrderService:
    def __init__(self):
        """Setup database connection and other properties"""
        self.connection = sqlite3.connect('/data/checkoutapp.db')
        self.connection.row_factory = sqlite3.Row
        pass

    def create_order(self, payment_info) -> (bool, List):
        """Creates all the database objects related to order"""
        validated, errors = validate_payload(payment_info)
        if not validated:
            return False, errors

        # create order object
        first_name = escape(payment_info['firstName'])
        last_name = escape(payment_info['lastName'])
        email = escape(payment_info['email'])
        order_id = self._store_order(first_name, last_name, email)

        # create order payment object
        payment_method = escape(payment_info['paymentMethod'])
        cc_name = escape(payment_info['ccName'])
        cc_number = escape(payment_info['ccNumber'])
        cc_expiration = escape(payment_info['ccExpiration'])
        cc_cvv = escape(payment_info['ccCVV'])
        self._store_order_payment_info(order_id, payment_method, cc_name, cc_number, cc_expiration, cc_cvv)

        # create order items object
        items = payment_info['items']
        check = self._store_order_items(order_id, items)

        self.connection.commit()
        return True, check

    def get_orders(self) -> Dict:
        """Get all orders with its items"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT Orders.id AS order_id, first_name, last_name, product_id, quantity FROM Orders "
                       "    INNER JOIN OrderItems ON Orders.id = OrderItems.order_id")
        orders = {}
        for row in cursor.fetchall():
            row = dict(row)
            key = row['order_id']
            if key not in orders:
                orders[key] = {
                    "firstName": row['first_name'],
                    "lastName": row['last_name'],
                    "items": []
                }

            orders[key]['items'].append({
                'productId': row['product_id'],
                "quantity": row['quantity']
            })

        return orders

    def _store_order(self, first_name, last_name, email) -> int:
        """Creates a row in Orders table with basic order information"""
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Orders (first_name, last_name, email) VALUES ('{first_name}', '{last_name}', '{email}')"
        )
        return cursor.lastrowid

    def _store_order_payment_info(self, order_id, payment_method, cc_name, cc_number, cc_expiration, cc_cvv) -> None:
        """Creates a row in orderPayment that stores payment information of an order"""
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO OrderPayment (order_id, payment_type, name_on_card, card_number, expiration, cvv)"
            f" VALUES ({order_id}, '{payment_method}', '{cc_name}', '{cc_number}', '{cc_expiration}', '{cc_cvv}')"
        )

    def _store_order_items(self, order_id, items) -> bool:
        """Store order's items"""
        cursor = self.connection.cursor()
        cursor.executemany(
            'INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (?, ?, ?)',
            [(order_id, item['id'], item['quantity']) for item in items]
        )
        return True
