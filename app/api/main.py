from fastapi import FastAPI

from api import recipe, ingredient

app = FastAPI()
app.include_router(router=recipe.router, prefix="/recipes")
app.include_router(router=ingredient.router, prefix="/ingredients")
