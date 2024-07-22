from flask import Flask, request
from waitress import serve
from project.image_scanning import run_resource_graph_query, send_to_queue
import json


app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    response = request.get_json()
    data = response["target"]["digest"]
    response = {"digest":data}
    # response = {"id": "16fb04ff-d60a-4dee-ac91-f9e7cce90f90", "timestamp": "2024-07-22T08:12:33.144561397Z", "action": "push", "target": {"mediaType": "application/vnd.docker.distribution.manifest.v2+json", "size": 3051, "digest": "sha256:b7b4bd1e521212bd236ce11d073be5b1952819f162f1cb9d1f07fda79215b377", "length": 3051, "repository": "image-scanning-code", "tag": "latest"}, "request": {"id": "80f46bf6-7d54-4085-9c0a-8724ad384fda", "host": "containerregistryautomationdev.azurecr.io", "method": "PUT", "useragent": "docker/26.1.3 go/go1.21.10 git-commit/8e96db1 kernel/6.5.0-1023-azure os/linux arch/amd64 UpstreamClient(Go-http-client/1.1)"}}
    # run_resource_graph_query(response["target"]["digest"], response["timestamp"])
    send_to_queue(response)
    return response



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
