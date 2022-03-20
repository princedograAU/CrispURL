import secrets

from django.conf import settings

from url_shorter.models import UrlShorter, UrlInputFields

RANDOM_STRING_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def get_random_string(length=settings.SHORT_URL_LENGTH, allowed_chars=RANDOM_STRING_CHARS):
    """
    Returns a random generated string of specified length. By default, the length is 8 characters longs
    Unique string generated strings can be calculated as follows:

    Total number of characters  : (26 + 26 + 10) RANDOM_STRING_CHARS
    Base value                  : 8
    Total permutations          : 2.1834011e+14

    example:
    >>> get_random_string()
    >>> 'AvBnn0re'
    """
    return ''.join(secrets.choice(allowed_chars) for i in range(length))


def generate_random_url(request_params: UrlInputFields):
    while True:
        random_string = get_random_string()
        try:
            url_obj = UrlShorter.objects.create(
                original_url=request_params.url,
                short_url=f"{settings.REDIRECT_URL}/{random_string}/",
                short_url_alias=random_string,
                hits=1
            )
            return url_obj
        except UrlShorter.DoesNotExist:
            return random_string
