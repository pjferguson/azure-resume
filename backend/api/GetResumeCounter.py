import azure.functions as func
import logging
from Counter import IdCount
from json import dumps

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="GetResumeCounter")
def GetResumeCounter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Connect to the Cosmos DB
    cosmos_client = cosmos_client.from_connection_string("AzureRConnectionString")
    database = cosmos_client.get_database_client("Resume-db")
    container = database.get_container_client("Counter")

    # Query the Cosmos DB for the counter
    for item in container.query_items(query='SELECT * FROM c WHERE c.id = "counter"',
        enable_cross_partition_query=True):
        counter = IdCount(item['id'], item['count'])
    
    if counter is None:
        counter = IdCount('counter', 0)
        container.create_item(body=counter.__dict__)
    
    counter.count += 1
    
    container.replace_item(item=counter.__dict__, body=counter.__dict__)

    return func.HttpResponse(json.dumps(counter.__dict__), mimetype="application/json", status_code=200)


        