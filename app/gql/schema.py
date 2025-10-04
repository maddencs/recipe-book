from typing import List

import strawberry

from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from database import Session
from gql.types import IngredientType, RecipeType, RecipeIngredientType
from models import Ingredient, Recipe, RecipeIngredient


def to_ingredient_type(ingredient: Ingredient) -> IngredientType:
    return IngredientType(id=ingredient.id, name=ingredient.name)


def to_recipe_type(recipe: Recipe) -> RecipeType:
    return RecipeType(
        id=recipe.id,
        name=recipe.name,
        recipe_ingredients=[
            RecipeIngredientType(
                ingredient=to_ingredient_type(ri.ingredient),
                quantity=ri.quantity,
                unit=ri.unit,
            ) for ri in recipe.recipe_ingredients
        ]
    )


@strawberry.type
class Query:
    @strawberry.field
    def recipes(self) -> List[RecipeType]:
        session = Session()
        try:
            stmt = select(Recipe).options(
                selectinload(Recipe.recipe_ingredients).selectinload(
                    RecipeIngredient.ingredient
                )
            )
            recipes = session.execute(stmt).scalars().all()
        finally:
            session.close()

        return [to_recipe_type(recipe) for recipe in recipes]


schema = strawberry.Schema(query=Query)
