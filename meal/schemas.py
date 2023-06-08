import datetime
from typing import List, Optional
from ninja import Schema
from base.schemas import QueryParamsSchema

from meal.models import MealFood
from food.schemas import FoodSimpleSchema


class MealFoodCreateParams(Schema):
    meal_type: MealFood.MealTypeChoices
    food_id: int
    custom_serving_id: Optional[int]
    quantity: float


class MealFoodSchema(Schema):
    class ServingSchema(Schema):
        amount: float
        unit: str

    id: int
    meal_type: MealFood.MealTypeChoices
    food: FoodSimpleSchema

    serving: ServingSchema

    served_energy: float
    served_protein: float
    served_carbohydrate: float
    served_sugar: Optional[float]
    served_sodium: Optional[float]


class MealSchema(Schema):
    date: datetime.date
    meal_type: MealFood.MealTypeChoices
    meal_foods: List[MealFoodSchema]


class MealListParams(QueryParamsSchema):
    created_at__gte: Optional[datetime.datetime]
    created_at__lte: Optional[datetime.datetime]
    meal_type: Optional[MealFood.MealTypeChoices]
