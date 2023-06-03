from ninja import NinjaAPI

api = NinjaAPI()

from meal.views import router as meal_router

api.add_router("meal/", meal_router)



