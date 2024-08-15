from azure.identity import DefaultAzureCredential
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.storage.queue import QueueClient, TextBase64EncodePolicy
from azure.mgmt.resourcegraph.models import QueryRequest
import os
import sys
import pika
import logging
import json


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config.config_variables


def run_resource_graph_query(image_digest,image_name,date):
    try:
        credential = DefaultAzureCredential()
        client = ResourceGraphClient(credential)
        query = set_resource_graph_query(image_digest,image_name)
        result = client.resources(QueryRequest(query=query)).as_dict()
        # send_message_to_rabbitmq(
        #     result,
        #     config.config_variables.host,
        #     config.config_variables.queue_name,
        #     config.config_variables.user_name,
        #     config.config_variables.password
        # )
        send_to_queue(
            config.config_variables.connection_string,
            config.config_variables.queue_name,
            result,
            date,
        )

    except Exception as ex:
        return str(ex)


def set_resource_graph_query(image_digest,image_name):
    query = f"""
        securityresources
        | where type =~ 'microsoft.security/assessments/subassessments'
        | where properties.resourceDetails.ResourceProvider == 'acr'
        | where properties contains '{image_digest}'
        | summarize data = make_list(pack(
            'CVE_ID', properties.id,
            'Severity', properties.additionalData.vulnerabilityDetails.severity
        )) by tostring(properties.resourceDetails.ResourceName)
        | project ImageName='{image_name}' , Data=data
    """
    return query


# def send_message_to_rabbitmq(message, host, queue, username, password):
#     try:
#         credentials = pika.PlainCredentials(username, password)
#         connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials))
#         channel = connection.channel()
#         channel.queue_declare(queue=queue)
#         channel.basic_publish(exchange='',
#                               routing_key=queue,
#                               body=str(message))
#         connection.close()
#         return 
        
#     except Exception as e:
#         logging.error(f"Error sending message to RabbitMQ: {e}")
    
def send_to_queue(connection_string, queue_name, json_message, date):
    try:
        queue_client = QueueClient.from_connection_string(
            connection_string,
            queue_name,
            message_encode_policy=TextBase64EncodePolicy(),
        )
        json_message["dateOfPush"] = date
        queue_client.send_message(json.dumps(json_message))
    except Exception as ex:
        raise Exception(ex)
    








    