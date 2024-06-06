import azure.functions as func
import logging
from azure.cosmos import CosmosClient
import json
import os
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="GetResumeCounter")
def GetResumeCounter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    connection_str = os.environ["AzureResumeConnectionStr"]
    Client = CosmosClient.from_connection_string(connection_str)
    database = Client.get_database_client("Resume-db")
    container = database.get_container_client("Counter")

    item_id = "1"

    try:
        item = container.read_item(item=item_id, partition_key="1")
        item['counter'] += 1
        container.replace_item(item=item_id, body=item)

        return func.HttpResponse(body=json.dumps({"id": item_id, "counter": item["counter"]}, indent=4), status_code=200, mimetype="application/json")
    except Exception as e:
        logging.error(f"Error updating item: {e} ")
        return func.HttpResponse(body=json.dumps({"error":"Error updating item."}), status_code=500, mimetype="application/json")
    