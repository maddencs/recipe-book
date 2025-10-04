from typing import List

import strawberry


@strawberry.type
class IngredientType:
    id: int
    name: str


@strawberry.type
class RecipeIngredientType:
    ingredient: IngredientType
    unit: str
    quantity: float


@strawberry.type
class RecipeType:
    id: int
    name: str
    recipe_ingredients: List[RecipeIngredientType]
