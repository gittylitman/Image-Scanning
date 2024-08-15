from flask import Flask, request
from waitress import serve
import time
from project.image_scanning import send_message_to_rabbitmq
import pika , logging

app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    return "kjhgfdsdfg"

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
