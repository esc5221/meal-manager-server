from typing import List, Optional

from ninja import Router, Schema

from base.schemas import QueryParamsSchema

router = Router(tags=["food"])


class FoodCreateSchema(Schema):
    category: str
    name: str

    serving_amount: float
    serving_unit: str

    energy: float
    protein: float
    carbohydrate: float
    sugar: Optional[float]
    sodium: Optional[float]
    manufacturer_id: Optional[int]


class FoodSchema(Schema):
    id: int
    db_group: str
    code: str

    category: str
    name: str

    serving_amount: float
    serving_unit: str

    energy: float
    protein: float
    carbohydrate: float
    sugar: Optional[float]
    sodium: Optional[float]
    manufacturer_id: Optional[int]


class FoodListParams(QueryParamsSchema):
    category__in: Optional[List[str]]
    name__icontains: Optional[str]
    manufacturer__name__icontains: Optional[str]

    by__category: Optional[int]
    by__name: Optional[int]
    by__manufacturer__name: Optional[int]


"""
"""


class FoodCategorySchema(Schema):
    category: str
    food_count: int


class FoodCategoryParams(QueryParamsSchema):
    category__icontains: Optional[str]

    by__category: Optional[int]
    by__food_count: Optional[int]
