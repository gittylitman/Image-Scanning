from flask import Flask, request
from waitress import serve
import logging
import pika


app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
    # def send_message_to_rabbitmq(message, host, queue, username, password):
    try:
        credentials = pika.PlainCredentials("admin", "admin")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="4.156.100.2", credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue="logs")
        channel.basic_publish(exchange='',
                              routing_key="logs",
                              body="hello rabbit:)")
        connection.close()
    except Exception as e:
        return "Error sending message to RabbitMQ: {e}"

    # # run_resource_graph_query(response["target"]["digest"],response["target"]["repository"], response["timestamp"])
    # # run_resource_graph_query("sha256:01bc7b5bf458832823d2c7334aeefa127a81296b0506d24852466781f760ee9c","services/storage_account/func_check_storage", "1-1-2003")
    # send_message_to_rabbitmq("tryyyy","4.156.100.2","logs","admin","admin")
    return "hellooooo"



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
