from flask import Flask, request
from waitress import serve
from project.image_scanning import run_resource_graph_query


app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    # response = request.get_json()
    # run_resource_graph_query(response["target"]["digest"],response["target"]["repository"], response["timestamp"])
    run_resource_graph_query("sha256:6b37597ee8a5601c23762453be959cc43c0689df6efd67f0c2f07db7636c9281","getmy-num", "1-1-2003")
    # return response



if __name__ == "__main__":
    send_to_image_scanning()
    serve(app, host="0.0.0.0", port=8080)
