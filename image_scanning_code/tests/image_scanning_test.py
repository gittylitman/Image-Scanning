from unittest.mock import patch, MagicMock
import json
from datetime import datetime
from project.image_scanning import (
    send_to_queue,
    set_resource_graph_query,
    run_resource_graph_query,
)
import config


@patch("project.image_scanning.DefaultAzureCredential")
@patch("project.image_scanning.ResourceGraphClient")
@patch("project.image_scanning.set_resource_graph_query")
@patch("project.image_scanning.send_to_queue")
def test_run_resource_graph_query(
    mock_send_to_queue,
    mock_set_resource_graph_query,
    mock_ResourceGraphClient,
    mock_DefaultAzureCredential,
):
    mock_credential = mock_DefaultAzureCredential.return_value
    mock_client = mock_ResourceGraphClient.return_value
    mock_client.resources.return_value.as_dict.return_value = {"mocked": "result"}
    mock_set_resource_graph_query.return_value = "mocked_query"
    resource_group_name = "test_rg"
    image_digest = "test_digest"
    date = "2023-06-13"
    result = run_resource_graph_query(resource_group_name, image_digest, date)
    mock_DefaultAzureCredential.assert_called_once()
    mock_ResourceGraphClient.assert_called_once_with(mock_credential)
    mock_set_resource_graph_query.assert_called_once_with(
        resource_group_name, image_digest
    )
    mock_client.resources.assert_called_once()
    mock_send_to_queue.assert_called_once_with(
        config.config_variables.connection_string,
        config.config_variables.queue_name,
        {"mocked": "result"},
        date,
    )
    assert result is None


@patch("project.image_scanning.DefaultAzureCredential")
@patch("project.image_scanning.ResourceGraphClient")
@patch("project.image_scanning.set_resource_graph_query")
@patch("project.image_scanning.send_to_queue")
def test_run_resource_graph_query_exception(
    mock_send_to_queue,
    mock_set_resource_graph_query,
    mock_ResourceGraphClient,
    mock_DefaultAzureCredential,
):
    mock_client = mock_ResourceGraphClient.return_value
    mock_client.resources.side_effect = Exception("Test Exception")
    resource_group_name = "test_rg"
    image_digest = "test_digest"
    date = "2023-06-13"
    result = run_resource_graph_query(resource_group_name, image_digest, date)
    assert result == "Test Exception"


@patch("azure.storage.queue.QueueClient.from_connection_string")
def test_send_to_queue(mock_from_connection_string):
    mock_queue_client_instance = MagicMock()
    mock_from_connection_string.return_value = mock_queue_client_instance

    connection_string = "fake_connection_string"
    queue_name = "test_queue"
    json_message = {"key": "value"}
    date = datetime.now().isoformat()

    send_to_queue(connection_string, queue_name, json_message, date)

    assert json_message["dateOfPush"] == date

    expected_message = json.dumps({"key": "value", "dateOfPush": date})
    mock_queue_client_instance.send_message.assert_called_once_with(expected_message)


def test_set_resource_graph_query():
    resource_group_name = "test_resource_group"
    image_digest = "test_image_digest"
    actual_query = set_resource_graph_query(resource_group_name, image_digest)
    assert isinstance(actual_query, str)
