import azure.functions as func
import logging
from Counter import IdCount
from azure.cosmos import CosmosClient

GetResumeCounter = func.Blueprint()


@GetResumeCounter.route(route="GetResumeCounter", auth_level=func.AuthLevel.ANONYMOUS)
def GetResumeCounter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    cosmos_db = CosmosClient.from_connection_string("AzureRString")
    database = CosmosClient.get_database_client("Resume-db")
    container = database.get_container_client("Counter")


    return "Running function locally, finish the code brother"

