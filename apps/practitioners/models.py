from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import FullNameModel, TimestampedModel


class Practitioner(FullNameModel, TimestampedModel):
    user = models.OneToOneField(
        on_delete=models.CASCADE,
        to="users.User",
        related_name="as_practitioner",
        unique=True,
    )
    speciality = models.ForeignKey(
        null=True,
        on_delete=models.PROTECT,
        to="practitioners.Speciality",
    )

    class Meta(TimestampedModel.Meta):
        default_related_name = "practitioners"

    def __str__(self):
        return self.full_name


class Speciality(TimestampedModel):
    is_active = models.BooleanField(default=True)
    name = models.CharField(db_index=True, max_length=512, unique=True)
    snomed_code = models.CharField(
        help_text=(_("Synonyms: `concept identifier`, `conceptid`.")),
        max_length=64,
    )
    snomed_name = models.CharField(max_length=512)

    class Meta(TimestampedModel.Meta):
        default_related_name = "specialties"

    def __str__(self):
        return self.name
