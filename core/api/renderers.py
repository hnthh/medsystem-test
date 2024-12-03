from djangorestframework_camel_case.render import CamelCaseJSONRenderer


class AppJSONRenderer(CamelCaseJSONRenderer):
    charset = "utf-8"
    json_underscoreize = {"no_underscore_before_number": True}
