import phonenumbers

from core.testing import register


@register
def phone_number(self):
    del self

    number = phonenumbers.example_number("RU")

    return phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
