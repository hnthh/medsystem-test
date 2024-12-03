from django.utils.translation import gettext_lazy as _

from core.models import TimestampedModel, models


class EncounterQuerySet(models.QuerySet):
    def for_view(self):
        return self.select_related(
            "location",
            "patient",
        ).order_by("-created_at", "-modified_at")


class Encounter(TimestampedModel):
    objects = models.Manager.from_queryset(EncounterQuerySet)()

    class Status(models.TextChoices):
        COMPLETED = "completed", _("Completed")
        CONFIRMED = "confirmed", _("Confirmed")
        PAID = "paid", _("Paid")
        PENDING = "pending", _("Pending")
        STARTED = "started", _("Started")

    location = models.ForeignKey("locations.Location", on_delete=models.PROTECT)
    patient = models.ForeignKey("patients.Patient", on_delete=models.CASCADE)
    practitioner = models.ForeignKey("practitioners.Practitioner", on_delete=models.PROTECT)
    status = models.CharField(choices=Status.choices, default=Status.STARTED, max_length=32)

    ended_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField()

    class Meta(TimestampedModel.Meta):
        default_related_name = "encounters"
