from core.testing import register


@register
def admin(self, **kwargs):
    return self.mixer.blend("admins.Admin", **kwargs)
