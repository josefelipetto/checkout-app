# Menu Checkout app
This applications is a Restaurant menu with checkout built in Vue 3 and Python (Flask)

# Installing
* Clone the repository on your local machine
* Make sure you have docker and docker-compose installed on your machine
* cd to Project root's folder
* Run `docker-compose down` for sanity check
* Run `docker-compose build --no-cache` to avoid any conflict with current cache from other projects
* Run `docker-compose up` or `docker-compose up -d` to run on background.

The application should start both containers in development mode and already created the database (Sqlite) with initial state

* Go to `http://localhost:8080`. The application should be running. 

# API Endpoints
| Endpoint        | Description | Example Payload |
| ------------- |:-------------:|:-------------: |
| GET menu/product | Returns a list of products | |
| GET menu/category | Returns a list of categories | |
| POST /order | Creates an order | See example below |
| GET /order | Returns a list of orders in the system | |

Example for **POST /order**
```json
{
  "orderInfo": {
    "firstName": "Some name",
    "lastName": "Some last name",
    "email": "someemail@example.com",
    "paymentMethod": "on",
    "ccName": "SOME NAME",
    "ccNumber": "99999999999999",
    "ccExpiration": "06/21",
    "ccCVV": "522",
    "items": [
      {
        "id": "1",
        "quantity": 5
      }
    ]
  }
}
```

