from flask import Flask, request
from waitress import serve
from azure.storage.queue import QueueClient, TextBase64EncodePolicy
import json, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    response = request.get_json()
    queue_client = QueueClient.from_connection_string(
            os.getenv("CONNECTION_STRING"),
            "try",
            message_encode_policy=TextBase64EncodePolicy(),
        )
    queue_client.send_message(json.dumps(response))
    return response


if __name__ == "__main__":
    print("start!!!")
    send_to_image_scanning()
    print("end!!!")
    serve(app, host="0.0.0.0", port=8080)