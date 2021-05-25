import sqlite3
from typing import List
from flask import escape
import sys


def validate_payload(payload) -> (bool, List):
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

    return has_errors, errors


class OrderService:
    def __init__(self):
        self.connection = sqlite3.connect('/data/checkoutapp.db')
        self.connection.row_factory = sqlite3.Row
        pass

    def create_order(self, payment_info) -> (bool, List):
        # validated, errors = validate_payload(payment_info)
        # if not validated:
        #     return False, errors

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

    def get_orders(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, first_name, last_name, product_id, quantity FROM Orders "
                       "    INNER JOIN OrderItems ON Orders.id = OrderItems.order_id")
        return [{"id": row['id'], ""} for row in cursor.fetchall()]

    def _store_order(self, first_name, last_name, email) -> int:
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Orders (first_name, last_name, email) VALUES ('{first_name}', '{last_name}', '{email}')"
        )
        return cursor.lastrowid

    def _store_order_payment_info(self, order_id, payment_method, cc_name, cc_number, cc_expiration, cc_cvv) -> None:
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO OrderPayment (order_id, payment_type, name_on_card, card_number, expiration, cvv)"
            f" VALUES ({order_id}, '{payment_method}', '{cc_name}', '{cc_number}', '{cc_expiration}', '{cc_cvv}')"
        )

    def _store_order_items(self, order_id, items) -> bool:
        cursor = self.connection.cursor()
        cursor.executemany(
            'INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (?, ?, ?)',
            [(order_id, item['id'], item['quantity']) for item in items]
        )
        return True
