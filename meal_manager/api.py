from ninja import NinjaAPI

api = NinjaAPI()

from food.views import router as food_router
from meal.views import router as meal_router

api.add_router("food/", food_router)
api.add_router("meal/", meal_router)
