from core.models import TimestampedModel, models


class Location(TimestampedModel):
    class Type(models.TextChoices):
        ASSISTANCE = "assistance"
        CHARITY = "charity"
        CLINIC = "clinic"
        CONTRACTOR = "contractor"
        EXTERNAL_CLINIC = "externalClinic"
        INSURANCE_COMPANY = "insuranceCompany"
        LABORATORY = "laboratory"
        ORGANIZATION = "organization"

    name = models.CharField(max_length=512)
    type = models.CharField(max_length=32, choices=Type.choices)

    # these fields should use standardized classifiers instead of free text fields
    legal_address = models.CharField(blank=True, max_length=1024)
    physical_address = models.CharField(blank=True, max_length=1024)

    class Meta(TimestampedModel.Meta): ...

    def __str__(self) -> str:
        return self.name
