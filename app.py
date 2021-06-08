from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def check_posted_data(posted_data, function_name):
    if "x" not in posted_data or "y" not in posted_data:
        return 301  # Missing parameter
    elif function_name == "divide" and int(posted_data["y"]) == 0:
        return 302  # Attempting to divide by 0
    return 200


def perform_operation(x, y, function_name):
    result = 0
    if function_name == "add":
        result = int(x) + int(y)
    elif function_name == 'subtract':
        result = int(x) - int(y)
    elif function_name == 'multiply':
        result = int(x) * int(y)
    elif function_name == 'divide':
        result = int(x) / int(y)

    return result


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
        else:
            # Valid status code received, continue
            result = perform_operation(posted_data["x"], posted_data["y"], "add")
            return_json = {
                'Message': result,
                'Status Code': status_code
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
        else:
            # Valid status code received, continue
            result = perform_operation(posted_data["x"], posted_data["y"], "subtract")

            # Create response message
            return_json = {
                'Message': result,
                'Status Code': status_code
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
        else:
            # Valid status code received, continue
            result = perform_operation(posted_data["x"], posted_data["y"], "multiply")

            # Create response message
            return_json = {
                'Message': result,
                'Status Code': status_code
            }
        return jsonify(return_json)


class Divide(Resource):
    def post(self):
        # Get POSTed data
        posted_data = request.get_json()

        # Verify POSTed data's contents and format
        status_code = check_posted_data(posted_data, "divide")
        if status_code == 301:
            return_json = {
                "Message": "Missing one or more parameters.",
                "Status Code": status_code
            }
        elif status_code == 302:
            return_json = {
                "Message": "Attempted to divide by zero.",
                "Status Code": status_code
            }
        else:
            # Valid status code received, continue
            result = perform_operation(posted_data["x"], posted_data["y"], "divide")

            # Create message
            return_json = {
                'Message': result,
                'Status Code': status_code
            }
        return jsonify(return_json)


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
