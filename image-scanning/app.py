from flask import Flask, request,jsonify
from waitress import serve

app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    data = request.json
    return data.get('name')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)