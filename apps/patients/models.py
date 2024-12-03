from phonenumber_field.modelfields import PhoneNumberField

from core.models import FullNameModel, TimestampedModel, models


class Patient(FullNameModel, TimestampedModel):
    user = models.OneToOneField(
        on_delete=models.CASCADE,
        to="users.User",
        related_name="as_patient",
        unique=True,
    )

    email = models.EmailField(db_index=True, null=False, unique=True)
    phone = PhoneNumberField(db_index=True, null=False, unique=True)

    class Meta(TimestampedModel.Meta):
        default_related_name = "patients"

    def __str__(self):
        return self.full_name
