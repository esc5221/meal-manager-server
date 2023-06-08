from typing import ForwardRef, List, Optional

from ninja import Field, Router, Schema

from base.schemas import QueryParamsSchema

router = Router(tags=["food"])


class CustomServingUnitCreateSchema(Schema):
    unit: str
    ratio: float


class CustomServingUnitSchema(Schema):
    unit: str
    ratio: float
    original_serving: Optional[str]

    def resolve_original_serving(self, obj):
        return f"1{obj.unit} = {obj.ratio} {obj.food.serving_unit}"


"""
"""


class ManufacturerCreateSchema(Schema):
    name: str


class ManufacturerSchema(Schema):
    id: int
    name: str


class ManufacturerListParams(QueryParamsSchema):
    name__icontains: Optional[str]
    food__category: Optional[str]

    by__name: Optional[int]


"""
"""


class FoodCreateSchema(Schema):
    category: str
    name: str

    serving_amount: float = Field(..., gt=0)
    serving_unit: str

    energy: float = Field(..., gt=0)
    protein: float = Field(..., gt=0)
    carbohydrate: float = Field(..., gt=0)
    sugar: Optional[float] = Field(..., gt=0)
    sodium: Optional[float] = Field(..., gt=0)
    manufacturer_id: Optional[int] = None


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
    manufacturer: ManufacturerSchema


class FoodDetailSchema(FoodSchema):
    customservingunit_set: List[CustomServingUnitSchema]


class FoodListParams(QueryParamsSchema):
    category__in: Optional[List[str]]
    name__icontains: Optional[str]
    manufacturer_id: Optional[int]

    by__category: Optional[int]
    by__name: Optional[int]


"""
"""


"""
"""


class FoodCategorySchema(Schema):
    category: str
    food_count: int


class FoodCategoryListParams(QueryParamsSchema):
    category__icontains: Optional[str]

    by__category: Optional[int]
    by__food_count: Optional[int]
