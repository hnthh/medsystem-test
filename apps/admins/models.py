from django.db import models

from core.models import FullNameModel, TimestampedModel


class Admin(FullNameModel, TimestampedModel):
    user = models.OneToOneField(
        on_delete=models.CASCADE,
        to="users.User",
        related_name="as_admin",
        unique=True,
    )

    class Meta(TimestampedModel.Meta):
        default_related_name = "admins"

    def __str__(self):
        return self.full_name
