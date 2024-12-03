class CurrentPractitionerDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context["request"].user.as_practitioner
