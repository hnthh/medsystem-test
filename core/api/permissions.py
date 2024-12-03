from rest_framework.permissions import IsAuthenticated


class AllowAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and hasattr(request.user, "as_admin")


class AllowPractitioner(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and hasattr(request.user, "as_practitioner")
