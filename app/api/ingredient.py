from typing import List

from fastapi import APIRouter, Depends

from database import Session
from models import Ingredient
from schemas.ingredient import IngredientOut

router = APIRouter()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[IngredientOut])
def get_ingredients(db: Session = Depends(get_db)):
    ingredients = db.query(Ingredient).all()
    return ingredients