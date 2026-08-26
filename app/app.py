from flask import Flask, request, jsonify

from app.calculator import add, subtract, multiply, divide

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Python Calculator API is running"
    })


@app.route("/add")
def addition():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    return jsonify({
        "result": add(a, b)
    })


@app.route("/subtract")
def subtraction():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    return jsonify({
        "result": subtract(a, b)
    })


@app.route("/multiply")
def multiplication():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    return jsonify({
        "result": multiply(a, b)
    })


@app.route("/divide")
def division():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    try:
        result = divide(a, b)
        return jsonify({"result": result})

    except ValueError as error:
        return jsonify({"error": str(error)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
