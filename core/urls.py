from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

ehr = [
    path("encounters/", include("apps.encounters.api.v1.ehr.urls")),
]

api = [
    path("ehr/", include(ehr)),
    path("token/obtain/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = [
    path("api/v1/", include(api)),
]
