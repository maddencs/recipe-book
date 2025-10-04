from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)


class Recipe(Base):
    __tablename__ = 'recipes'

    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(
        back_populates="recipe",
        cascade="all, delete-orphan",
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Ingredient(Base):
    __tablename__ = 'ingredients'

    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(
        back_populates="ingredient", cascade="all, delete-orphan"
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

#
class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'

    recipe_id: Mapped[int] = mapped_column(ForeignKey('recipes.id', ondelete='CASCADE'),
                                           primary_key=True)
    ingredient_id: Mapped[int] = mapped_column(ForeignKey('ingredients.id', ondelete='CASCADE'),
                                               primary_key=True)

    ingredient: Mapped[Ingredient] = relationship("Ingredient", back_populates="recipe_ingredients")
    recipe: Mapped[Recipe] = relationship("Recipe", back_populates="recipe_ingredients")

    quantity: Mapped[float] = mapped_column(Float, nullable=False)
    unit: Mapped[str] = mapped_column(String, nullable=False)
