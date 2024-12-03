from core.testing import register


@register
def user(self, **kwargs):
    return self.mixer.blend("users.User", **kwargs)
