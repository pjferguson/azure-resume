from unittest.mock import MagicMock, patch
from azure.cosmos import CosmosClient
from Function_app import GetResumeCounter
import json
from azure.functions import HttpRequest

def test_GetResumeCounter():
    # Mocking the HttpRequest object
    req = HttpRequest("GET", "http://localhost:7071/api/GetResumeCounter", body='')

    # Mocking the CosmosClient object
    cosmos_client = MagicMock(spec=CosmosClient)
    database_client = MagicMock()
    container_client = MagicMock()

    item = {"id": "1", "counter": 0}
    container_client.read_item.return_value = item
    container_client.replace_item.return_value = item

    database_client.get_container_client.return_value = container_client
    cosmos_client.get_database_client.return_value = database_client

    with patch('azure.cosmos.CosmosClient.from_connection_string', return_value=cosmos_client):
        response = GetResumeCounter(req)

    assert response.status_code == 200
    assert response.get_body() == json.dumps({"id": "1", "counter": 1}, indent=4)










        



