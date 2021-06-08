from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def check_posted_data(posted_data, function_name):
    if function_name == "add" or function_name == "subtract" or function_name == "multiply":
        if "x" not in posted_data or "y" not in posted_data:
            return 301  # Missing parameter
    elif function_name == "divide":
        if "x" not in posted_data or "y" not in posted_data:
            return 301  # Missing parameter
        elif posted_data["y"] == 0:
            return 302  # Attempting to divide by 0
    return 200


class Add(Resource):
    def post(self):
        # Get POSTed data
        posted_data = request.get_json()

        # Verify POSTed data's contents and format
        status_code = check_posted_data(posted_data, "add")
        if status_code != 200:
            return_json = {
                "Message": "Missing one or more parameters.",
                "Status Code": status_code
            }
            return jsonify(return_json)

        # Valid status code received, continue
        x = posted_data["x"]
        y = posted_data["y"]

        # Add POSTed data
        x_int = int(x)
        y_int = int(y)
        sum_result = x_int + y_int

        # Create message
        return_json = {
            'Message': sum_result,
            'Status Code': 200
        }
        return jsonify(return_json)


class Subtract(Resource):
    def post(self):
        # Get POSTed data
        posted_data = request.get_json()

        # Verify POSTed data's contents and format
        status_code = check_posted_data(posted_data, "subtract")
        if status_code != 200:
            return_json = {
                "Message": "Missing one or more parameters.",
                "Status Code": status_code
            }
            return jsonify(return_json)

        # Valid status code received, continue
        x = posted_data["x"]
        y = posted_data["y"]

        # Subtract POSTed data
        x_int = int(x)
        y_int = int(y)
        subtract_result = x_int - y_int

        # Create message
        return_json = {
            'Message': subtract_result,
            'Status Code': 200
        }
        return jsonify(return_json)


class Multiply(Resource):
    def post(self):
        # Get POSTed data
        posted_data = request.get_json()

        # Verify POSTed data's contents and format
        status_code = check_posted_data(posted_data, "multiply")
        if status_code != 200:
            return_json = {
                "Message": "Missing one or more parameters.",
                "Status Code": status_code
            }
            return jsonify(return_json)

        # Valid status code received, continue
        x = posted_data["x"]
        y = posted_data["y"]

        # Multiply POSTed data
        x_int = int(x)
        y_int = int(y)
        multiply_result = x_int * y_int

        # Create message
        return_json = {
            'Message': multiply_result,
            'Status Code': 200
        }
        return jsonify(return_json)


class Divide(Resource):
    def post(self):
        # Get POSTed data
        posted_data = request.get_json()

        # Verify POSTed data's contents and format
        status_code = check_posted_data(posted_data, "multiply")
        if status_code == 301:
            return_json = {
                "Message": "Missing one or more parameters.",
                "Status Code": status_code
            }
            return jsonify(return_json)
        elif status_code == 302:
            return_json = {
                "Message": "Attempted to divide by zero.",
                "Status Code": status_code
            }
            return jsonify(return_json)

        # Valid status code received, continue
        x = posted_data["x"]
        y = posted_data["y"]

        # Multiply POSTed data
        x_int = int(x)
        y_int = int(y)
        divide_result = x_int / y_int

        # Create message
        return_json = {
            'Message': divide_result,
            'Status Code': 200
        }
        return jsonify(return_json)


api.add_resource(Add, "/add")


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
