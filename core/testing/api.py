import json

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class DRFClient(APIClient):
    def __init__(self, user=None, **kwargs):
        super().__init__(**kwargs)

        self.user = user

        if self.user is not None:
            self.authenticate()

    def authenticate(self):
        token = Token.objects.get_or_create(user=self.user)[0]

        self.credentials(
            HTTP_AUTHORIZATION=f"Token {token}",
        )

    def logout(self):
        self.credentials()

        super().logout()

    def get(self, *args, **kwargs):
        return self._api_call("get", kwargs.get("expected_status_code", 200), *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._api_call("post", kwargs.get("expected_status_code", 201), *args, **kwargs)

    def put(self, *args, **kwargs):
        return self._api_call("put", kwargs.get("expected_status_code", 200), *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self._api_call("patch", kwargs.get("expected_status_code", 200), *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._api_call("delete", kwargs.get("expected_status_code", 204), *args, **kwargs)

    def _api_call(self, method, expected, *args, **kwargs):
        kwargs["format"] = kwargs.get("format", "json")
        as_response = kwargs.pop("as_response", False)

        method = getattr(super(), method)
        response = method(*args, **kwargs)

        if as_response:
            return response

        content = self._decode(response)

        assert response.status_code == expected, f'Got {response.status_code} instead of {expected}. Content is "{content}"'  # noqa: S101

        return content

    def _decode(self, response):
        content = response.content.decode("utf-8", errors="ignore")
        if self.is_json(response):
            return json.loads(content)

        return content

    @staticmethod
    def is_json(response):
        if response.has_header("content-type"):
            return "json" in response.get("content-type")

        return False
