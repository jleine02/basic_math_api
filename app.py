from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


def check_posted_data(posted_data, function_name):
    if function_name == "add":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        else:
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
        return_map = {
            'Message': sum_result,
            'Status Code': 200
        }
        return jsonify(return_map)


class Subtract(Resource):
    pass


class Multiply(Resource):
    pass


class Divide(Resource):
    pass


api.add_resource(Add, "/add")


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
