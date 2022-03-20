from django.test import TestCase

from url_shorter.models import UrlShorter


class TestUrlShorterModel(TestCase):

    def test_create(self):
        UrlShorter.objects.create(
            original_url="http://www.wikipedia.com",
            short_url="http://testserver/ABCDEFGI/",
            short_url_alias="ABCDEFGI",
            hits=1
        )

        self.assertEqual(UrlShorter.objects.count(), 1)

    def test_validate_short_url_alias(self):
        obj = UrlShorter.objects.create(
            original_url="http://www.wikipedia.com",
            short_url="http://testserver/ABCDEFGI/",
            short_url_alias="ABCDEFGI",
            hits=1
        )
        self.assertEqual(UrlShorter.objects.count(), 1)
