from flask import Flask, request
from waitress import serve
import time
from project.image_scanning import run_resource_graph_query, send_to_queue


app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    time.sleep(300)
    response = request.get_json()
    run_resource_graph_query(response["target"]["digest"],response["target"]["repository"], response["timestamp"])
    return response



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
