from flask import Flask, request
from waitress import serve
import logging
import pika


app = Flask(__name__)


@app.route("/image_push_acr", methods=["POST"])
def send_to_image_scanning():
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
    return "hellooooo"



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
