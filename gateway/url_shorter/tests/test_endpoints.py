from django.test import TestCase
from django.shortcuts import reverse

from rest_framework.exceptions import ErrorDetail

from commons.utils.testing import BaseEndpointTestMixin
from url_shorter.models import UrlShorter


class TestURLShorterEndpoint(BaseEndpointTestMixin, TestCase):
    ENDPOINT = reverse('short-url')
    NOT_ALLOWED_METHODS = ('delete', 'patch', 'put')

    def test_endpoint_new_entry(self):
        response = self.client.post(
            self.client_endpoint,
            {
                "url": "https://www.google.com"
            }
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(UrlShorter.objects.count(), 1)

    def test_create_existing_original_url(self):
        UrlShorter.objects.create(
            original_url="http://dummy.com",
            short_url="http://localhost.com/ABCDEFGH/",
            hits=1
        )
        response = self.client.post(
            self.client_endpoint,
            {
                "url": "http://dummy.com"
            }
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(UrlShorter.objects.count(), 2)
        obj = UrlShorter.objects.first()
        self.assertNotEqual(obj.short_url_alias, "ABCDEFGH")

    def test_create_not_a_url(self):
        cases = ("abc@dummy.com", "1234", "www.abc")
        expected_response = {'url': [ErrorDetail(string='Enter a valid URL.', code='invalid')]}
        for index, url in enumerate(cases):
            with self.subTest(index):
                response = self.client.post(
                    self.client_endpoint,
                    {
                        "url": url
                    }
                )

                self.assertEqual(response.status_code, 400)
                self.assertEqual(response.data, expected_response)

    def test_list_urls(self):
        UrlShorter.objects.create(
            original_url="http://dummy.com",
            short_url="http://localhost.com/ABCDEFGH/",
            short_url_alias="ABCDEFGH",
            hits=1
        )
        UrlShorter.objects.create(
            original_url="http://www.wikipedia.com",
            short_url="http://testserver/ABCDEFGI/",
            short_url_alias="ABCDEFGI",
            hits=1
        )

        response = self.client.get(self.client_endpoint)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_list_urls_not_available(self):
        response = self.client.get(self.client_endpoint)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_retrieve_url_successful(self):
        UrlShorter.objects.create(
            original_url="http://www.google.com",
            short_url="http://testserver/ABCDEFGH/",
            short_url_alias="ABCDEFGH",
            hits=1
        )
        UrlShorter.objects.create(
            original_url="http://www.wikipedia.com",
            short_url="http://testserver/ABCDEFGI/",
            short_url_alias="ABCDEFGI",
            hits=1
        )

        expected_response = {'original_url': 'http://www.google.com', 'short_url': 'http://testserver/ABCDEFGH/',
                             'count': 2}

        response = self.client.get(self.client_endpoint + "?url=http://testserver/ABCDEFGH/", follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_response)

    def test_retrieve_url_unsuccessful(self):
        expected_response = {'detail': ErrorDetail(string='Not found.', code='not_found')}
        response = self.client.get(self.client_endpoint + "?url=ABCDEFGH", follow=True)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, expected_response)

    def test_throttling(self):
        expected_response = {
            'detail': ErrorDetail(string='Request was throttled. Expected available in 60 seconds.', code='throttled')
        }
        for counter in range(0, 101):
            response = self.client.post(
                self.client_endpoint,
                {
                    "url": "https://www.google.com"
                }
            )
        self.assertEqual(response.status_code, 429)
        self.assertEqual(response.data, expected_response)
