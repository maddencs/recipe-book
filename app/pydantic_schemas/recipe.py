from typing import List, Optional

from pydantic import BaseModel


class IngredientOnly(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class RecipeIngredientOut(BaseModel):
    ingredient: IngredientOnly
    quantity: float
    unit: str

    class Config:
        orm_mode = True


class RecipeBase(BaseModel):
    name: str


class RecipeCreate(RecipeBase):
    ingredients: Optional[List] = None


class RecipeOut(RecipeBase):
    id: int
    recipe_ingredients: List[RecipeIngredientOut] = []

    class Config:
        orm_mode = True
