import azure.functions as func
import logging
from azure.cosmos import CosmosClient
import json
import 

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="GetResumeCounter")
def GetResumeCounter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    Client = CosmosClient.from_connection_string("AzureResumeConnectionStr")
    database = Client.get_database_client("Resume-db")
    container = database.get_container_client("Counter")

    req_body = req.get_json()
    item_id = req_body.get('id')

    try:
        item = container.read_item(item=item_id)
        item['counter'] += 1
        container.replace_item(item=item_id, body=item)

        return func.HttpResponse( body="Item updated successfully.", status_code=20)
    except Exception as e:
        logging.error(f"Error updating item: {e} ")
        return func.HttpResponse("Error updating item.", status_code=500)
    