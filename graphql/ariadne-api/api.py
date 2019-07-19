from ariadne import load_schema_from_path, QueryType, make_executable_schema
from ariadne.asgi import GraphQL


# load schema from file...
schema = load_schema_from_path("schema.graphql")


# Create type instance for Query type defined in our schema...
query = QueryType()


@query.field("Film")
def resolve_film(*_, title):
    #...
    pass


# executable_schema = make_executable_schema(schema, query)
# app = GraphQL(executable_schema, debug=True)
