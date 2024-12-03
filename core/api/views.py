from rest_framework.viewsets import ModelViewSet


class SerializerActionClassesMixin:
    def get_serializer_class(self):
        if self.action in self.serializer_action_classes:
            return self.serializer_action_classes[self.action]

        return super().get_serializer_class()


class BaseModelViewSet(SerializerActionClassesMixin, ModelViewSet):
    http_method_names = ["delete", "get", "head", "options", "patch", "post"]

    serializer_action_classes = {}
