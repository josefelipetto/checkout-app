from typing import List


class CategoryService:
    def __init__(self):
        pass

    def get_categories(self) -> List:
        return [
            {
                "id": 1,
                "image_id": "f3fbf57b118fa9",
                "name": "Bakery"
            },
            {
                "id": 2,
                "image_id": "b271afbefdc554",
                "name": "Entrees"
            },
            {
                "id": 3,
                "image_id": "eba73b2361fae3",
                "name": "Drinks"
            },
            {
                "id": 4,
                "image_id": "eba73b2361fae3",
                "name": "Drinks Some"
            }
        ]
