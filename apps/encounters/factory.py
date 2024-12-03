from core.testing import register


@register
def encounter(self, **kwargs):
    return self.mixer.blend("encounters.Encounter", **kwargs)
