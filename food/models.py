from django.db import models
from base.models import BaseModel


class Food(BaseModel):
    db_group = models.CharField(max_length=50, null=True)
    code = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=100)

    name = models.CharField(max_length=100)

    serving_amount = models.DecimalField(
        "serving_amount", max_digits=8, decimal_places=2, null=True
    )
    serving_unit = models.CharField(max_length=50)

    energy = models.DecimalField(
        "energy(kcal)", max_digits=8, decimal_places=2, null=True
    )
    protein = models.DecimalField("protein(g)", max_digits=8, decimal_places=2)
    carbohydrate = models.DecimalField(
        "carbohydrate(g)", max_digits=8, decimal_places=2, null=True
    )
    sugar = models.DecimalField("sugar(g)", max_digits=8, decimal_places=2, null=True)
    sodium = models.DecimalField(
        "sodium(mg)", max_digits=8, decimal_places=2, null=True
    )

    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, null=True
    )


class CustomServingUnit(BaseModel):
    food = models.ForeignKey("Food", on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, unique=True)
    ratio = models.DecimalField(max_digits=8, decimal_places=2)


class Manufacturer(BaseModel):
    name = models.CharField(max_length=100, unique=True)
