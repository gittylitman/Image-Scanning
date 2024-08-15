from flask import Flask, request
from waitress import serve
from project.image_scanning import run_resource_graph_query, send_message_to_rabbitmq


app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    response = request.get_json()
    run_resource_graph_query(response["target"]["digest"],response["target"]["repository"], response["timestamp"])
    # run_resource_graph_query("sha256:01bc7b5bf458832823d2c7334aeefa127a81296b0506d24852466781f760ee9c","services/storage_account/func_check_storage", "1-1-2003")
    return response



if __name__ == "__main__":
    send_to_image_scanning()
    serve(app, host="0.0.0.0", port=8080)
