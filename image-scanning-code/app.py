from flask import Flask, request
from waitress import serve
from project.image_scanning import run_resource_graph_query, send_to_queue


app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    # response = request.get_json()
    # response = {response["target"]["digest"],response["target"]["repository"], response["timestamp"]}
    # send_to_queue(response)
    run_resource_graph_query("sha256:b9ef223e0f9eb5f3cfb50b2b644ef12d2719abe0e9c6f9b0ab370d4554c54bdc","services/laravel/func_try_users")
    # return response



if __name__ == "__main__":
#     res = {
#   "id": "444242f7-c3f6-4f57-b2aa-bcab19274d21",
#   "timestamp": "2024-08-12T09:16:59.3634728Z",
#   "action": "push",
#   "target": {
#     "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
#     "size": 3051,
#     "digest": "sha256:5a9727c22f23a65d3648af746e541b65769df572147c9d25a072f7ee7c70dc5e",
#     "length": 3051,
#     "repository": "upload",
#     "tag": "latest"
#   },
#   "request": {
#     "id": "142dc81b-5720-4bc6-8f33-3568949c5786",
#     "host": "containerregistryautomationdev.azurecr.io",
#     "method": "PUT",
#     "useragent": "docker/26.1.3 go/go1.21.10 git-commit/8e96db1 kernel/6.5.0-1025-azure os/linux arch/amd64 UpstreamClient(Go-http-client/1.1)"
#   }
# }

#     send_to_image_scanning(res)
    serve(app, host="0.0.0.0", port=8080)
