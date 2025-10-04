from fastapi import FastAPI

from api import recipe, ingredient
from gql.router import gql_router

app = FastAPI()
app.include_router(router=recipe.router, prefix="/recipes")
app.include_router(router=ingredient.router, prefix="/ingredients")
app.include_router(router=gql_router, prefix="/graphql")
