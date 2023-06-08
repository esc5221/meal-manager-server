from typing import Optional
from django.db import models
from django.utils.functional import cached_property

from base.models import CommonModel
from user.models import User
from food.models import Food, CustomServingUnit


class MealFood(CommonModel):
    class MealTypeChoices(models.TextChoices):
        breakfast = "breakfast", "아침"
        lunch = "lunch", "점심"
        dinner = "dinner", "저녁"
        snack = "snack", "간식"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(
        max_length=10, choices=MealTypeChoices.choices, default=MealTypeChoices.snack
    )
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    custom_serving = models.ForeignKey(
        CustomServingUnit, on_delete=models.CASCADE, null=True
    )
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    @cached_property
    def serving_amount_multiplier(self) -> float:
        if self.custom_serving:
            return self.custom_serving.ratio
        else:
            return 1

    def get_served_value(self, field_name: str) -> Optional[float]:
        if not hasattr(self.food, field_name):
            raise ValueError(f"Field name {field_name} does not exist")
        value = getattr(self.food, field_name)
        if value is None:
            return None
        return (
            float(value) * float(self.quantity) * float(self.serving_amount_multiplier)
        )

    @cached_property
    def serving(self) -> dict:
        if self.custom_serving:
            return {
                "amount": self.custom_serving.ratio * self.quantity,
                "unit": self.custom_serving.unit,
            }
        else:
            return {
                "amount": self.food.serving_amount * self.quantity,
                "unit": self.food.serving_unit,
            }

    @cached_property
    def served_energy(self) -> float:
        return self.get_served_value("energy")

    @cached_property
    def served_protein(self) -> float:
        return self.get_served_value("protein")

    @cached_property
    def served_carbohydrate(self) -> float:
        return self.get_served_value("carbohydrate")

    @cached_property
    def served_sugar(self) -> float:
        return self.get_served_value("sugar")

    @cached_property
    def served_sodium(self) -> float:
        return self.get_served_value("sodium")
