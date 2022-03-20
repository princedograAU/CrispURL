from rest_framework.test import APIClient


class BaseEndpointTestMixin:
    ENDPOINT = None
    NOT_ALLOWED_METHODS = ('get', 'post', 'delete', 'patch', 'put')

    def __init__(self, *args, **kwargs):
        try:
            if self.ENDPOINT:
                self.client_endpoint = f'http://testserver' + self.__class__.ENDPOINT
        except AttributeError:
            pass

        super().__init__(*args, **kwargs)

    def setUp(self):
        self.client = APIClient()
