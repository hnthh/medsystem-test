from core.testing import register


@register
def patient(self, **kwargs):
    return self.mixer.blend("patients.Patient", **kwargs)
