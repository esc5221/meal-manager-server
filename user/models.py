from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class User(AbstractUser):
    first_name = None
    last_name = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.email


class Profile(BaseModel):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    birth_year = models.IntegerField(_("birth year"), null=True)
    weight = models.DecimalField(
        _("weight(kg)"), max_digits=5, decimal_places=2, null=True
    )
    height = models.DecimalField(
        _("height(cm)"), max_digits=5, decimal_places=2, null=True
    )
