from typing import List, Optional, Dict

from ninja import Query, Router, Schema
from ninja.pagination import paginate

from base.schemas import QueryParamsSchema
from food.schemas import (
    FoodCategoryParams,
    FoodCategorySchema,
    FoodListParams,
    FoodSchema,
)

router = Router(tags=["food"])


from django.db.models import Count
from food.models import Food


@router.get(
    "/list",
    response={200: List[FoodSchema]},
)
@paginate()
def list_food(request, params: FoodListParams = Query(...)):
    return Food.objects.filter(**params.filters()).order_by(*params.orders())


@router.get(
    "/category",
    response={200: List[FoodCategorySchema]},
)
@paginate()
def list_category(request, params: FoodCategoryParams = Query(...)):
    return (
        Food.objects.values("category")
        .annotate(food_count=Count("category"))
        .filter(**params.filters())
        .order_by(*params.orders())
    )
