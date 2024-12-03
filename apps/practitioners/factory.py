from core.testing import register


@register
def practitioner(self, **kwargs):
    return self.mixer.blend("practitioners.Practitioner", **kwargs)
