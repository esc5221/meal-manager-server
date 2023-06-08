from django.conf import settings
from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(auth=django_auth, csrf=True)

from user.views import router as user_router
from food.views import router as food_router
from meal.views import router as meal_router

api.add_router("users/", user_router)
api.add_router("foods/", food_router)
api.add_router("meals/", meal_router)

from meal_manager.exceptions import api_exception_response

if not settings.DEBUG:

    @api.exception_handler(Exception)
    def api_exception_handler(request, exc):
        response, status_code = api_exception_response(request, exc)
        return api.create_response(request, response, status=status_code)
