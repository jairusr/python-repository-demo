from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/multiply', methods=['GET'])
@swag_from
def multiply():
    """
    Multiply two numbers
    ---
    parameters:
      - name: x
        in: query
        type: number
        required: true
      - name: y
        in: query
        type: number
        required: true
    responses:
      200:
        description: The result of the multiplication
    """
    x = request.args.get("x", type=float)
    y = request.args.get("y", type=float)
    result = x * y
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
