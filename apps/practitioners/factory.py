from core.testing import register


@register
def practitioner(self, **kwargs):  # noqa: ARG001
    return self.mixer.blend("practitioners.Practitioner")
