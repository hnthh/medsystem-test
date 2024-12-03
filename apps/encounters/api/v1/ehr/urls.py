from django.urls import include, path
from rest_framework.routers import SimpleRouter

from apps.encounters.api.v1.ehr import views

router = SimpleRouter()

router.register("", views.EncounterView)

urlpatterns = [
    path("", include(router.urls)),
]
