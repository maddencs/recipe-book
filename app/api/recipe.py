from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from database import Session
from models import Recipe, RecipeIngredient
from schemas.recipe import RecipeOut, RecipeCreate


router = APIRouter()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[RecipeOut])
def get_recipes(db: Session = Depends(get_db)):
    stmt = (
        select(Recipe)
        .options(
            selectinload(Recipe.recipe_ingredients).selectinload(RecipeIngredient.ingredient)
        )
    )
    recipes = db.execute(stmt).scalars().all()
    return recipes


@router.get("/{recipe_id}")
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).get(recipe_id)
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': [
            {
                'id': ri.ingredient.id,
                'name': ri.ingredient.name,
                'quantity': ri.quantity,
                'unit': ri.unit,
            } for ri in recipe.recipe_ingredients
        ],
    }


@router.post("/", response_model=RecipeOut)
def create_recipe(recipe_in: RecipeCreate, db: Session = Depends(get_db)):
    recipe = Recipe(name=recipe_in.name)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)

    return recipe