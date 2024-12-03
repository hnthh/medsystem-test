from core.testing import register


@register
def location(self, **kwargs):
    return self.mixer.blend("locations.Location", **kwargs)
