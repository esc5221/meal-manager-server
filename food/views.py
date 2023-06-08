from typing import List, Optional, Dict

from ninja import Query, Router, Schema
from ninja.pagination import paginate

from base.schemas import QueryParamsSchema
from food.schemas import (
    CustomServingUnitCreateSchema,
    CustomServingUnitSchema,
    FoodCategoryListParams,
    FoodCategorySchema,
    FoodCreateSchema,
    FoodDetailSchema,
    FoodListParams,
    FoodSchema,
    ManufacturerListParams,
    ManufacturerSchema,
)

router = Router(tags=["foods"])


from django.db.models import Count
from food.models import CustomServingUnit, Food, Manufacturer


@router.get(
    "/food/list",
    response={200: List[FoodSchema]},
)
@paginate()
def list_food(request, params: FoodListParams = Query(...)):
    return (
        Food.objects.filter(**params.filters())
        .order_by(*params.orders())
        .select_related("manufacturer")
    )


@router.post(
    "/food",
    response={200: FoodCreateSchema},
)
def post_food(request, params: FoodCreateSchema):
    return Food.objects.create(**params.dict())


@router.get(
    "/food/{food_id}",
    response={200: FoodDetailSchema},
)
def get_food(request, food_id: int):
    return Food.objects.get(id=food_id)


@router.post(
    "/food/{food_id}/custom_serving",
    response={200: FoodDetailSchema},
)
def create_custom_serving(request, food_id, params: CustomServingUnitCreateSchema):
    custom_serving = CustomServingUnit.objects.create(food_id=food_id, **params.dict())
    return custom_serving.food


"""
"""


@router.get("/manufacturer/list", response={200: List[ManufacturerSchema]})
@paginate()
def list_manufacturer(request, params: ManufacturerListParams = Query(...)):
    return (
        Manufacturer.objects.filter(**params.filters())
        .order_by(*params.orders())
        .distinct()
    )


"""
"""


@router.get(
    "/category",
    response={200: List[FoodCategorySchema]},
)
@paginate()
def list_food_category(request, params: FoodCategoryListParams = Query(...)):
    return (
        Food.objects.values("category")
        .annotate(food_count=Count("category"))
        .filter(**params.filters())
        .order_by(*params.orders())
        .distinct()
    )
