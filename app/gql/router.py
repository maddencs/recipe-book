from strawberry.fastapi import GraphQLRouter

from gql.schema import schema

gql_router = GraphQLRouter(schema=schema)
