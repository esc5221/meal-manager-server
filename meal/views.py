from datetime import datetime
from typing import Dict, List
from ninja import Query, Router
from ninja.pagination import paginate

from meal.models import MealFood
from meal.schemas import (
    MealFoodCreateParams,
    MealFoodSchema,
    MealListParams,
    MealSchema,
)

router = Router(tags=["meals"])


@router.post("/meal_food", response={200: MealFoodSchema})
def create_meal_food(request, params: MealFoodCreateParams):
    meal_food = MealFood.objects.create(
        user=request.user,
        meal_type=params.meal_type,
        food_id=params.food_id,
        custom_serving_id=params.custom_serving_id,
        quantity=params.quantity,
    )
    return meal_food


@router.get("/meal", response={200: List[MealSchema]})
@paginate()
def list_meals(request, params: MealListParams = Query(...)):
    meal_foods = (
        MealFood.objects.filter(**params.filters())
        .order_by(*params.orders())
        .select_related("food", "custom_serving")
    )

    date__type__foods: Dict[
        datetime.datetime, Dict[MealFood.MealTypeChoices, List[MealFood]]
    ] = {}
    for meal_food in meal_foods:
        date__type__foods.setdefault(meal_food.created_at.date(), {})
        date__type__foods[meal_food.created_at.date()].setdefault(
            meal_food.meal_type, []
        )
        date__type__foods[meal_food.created_at.date()][meal_food.meal_type].append(
            meal_food
        )

    return [
        MealSchema(
            date=date,
            meal_type=meal_type,
            meal_foods=[MealFoodSchema.from_orm(meal_food) for meal_food in meal_foods],
        )
        for date, meal_type__foods in date__type__foods.items()
        for meal_type, meal_foods in meal_type__foods.items()
    ]
