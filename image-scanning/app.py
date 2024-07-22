from flask import Flask, request
from waitress import serve
from azure.storage.queue import QueueClient, TextBase64EncodePolicy
import json

app = Flask(__name__)

@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    response = request.get_json()
    queue_client = QueueClient.from_connection_string(
            "DefaultEndpointsProtocol=https;AccountName=bycheckloganalytics;AccountKey=v35OL/fIulFJ44YVjxnZPLHPrAp67tq63B5vKksyGY2NlDuMlo5Pb/20AdeT4oqaIs3TuaNW9T1x+ASt09POGA==;EndpointSuffix=core.windows.net",
            "try",
            message_encode_policy=TextBase64EncodePolicy(),
        )
    queue_client.send_message(json.dumps(response))
    return response


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)