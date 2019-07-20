from ariadne import load_schema_from_path, QueryType, make_executable_schema
from ariadne.asgi import GraphQL
import logging
import requests


# load schema from file...
schema = load_schema_from_path("schema.graphql")


# Create type instance for Query type defined in our schema...
query = QueryType()


@query.field("Planet")
def resolve_planet(*_, name):
    logging.info("Making API request to swapi.co")
    response = requests.get("https://swapi.co/api/planets").json()
    for planet in response["results"]:
        if planet["name"] == name:
            residents = []
            for api_url in planet["residents"]:
                logging.info("Making API request to swapi.co")
                response = requests.get(api_url).json()
                residents.append({"name": response["name"], "height": response["height"]})
            return {"name": name, "residents": residents}


executable_schema = make_executable_schema(schema, query)
app = GraphQL(executable_schema, debug=True)
