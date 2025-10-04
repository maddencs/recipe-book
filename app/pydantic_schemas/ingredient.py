from pydantic import BaseModel


class IngredientBase(BaseModel):
    name: str


class IngredientCreate(IngredientBase):
    pass


class IngredientOut(IngredientBase):
    id: int

    class Config:
        orm_mode = True
