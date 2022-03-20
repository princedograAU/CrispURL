from dataclasses import dataclass
from uuid import uuid4

from django.db import models
from django.core.validators import RegexValidator

from commons.models import TimestampedModel


class UrlShorter(TimestampedModel):
    id = models.UUIDField(primary_key=True, null=False, db_index=True, editable=False, default=uuid4)
    original_url = models.URLField(max_length=255)
    short_url = models.URLField(max_length=255)
    short_url_alias = models.CharField(max_length=50, unique=True, db_index=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9]{8}$',
            code='invalid_url_suffix',
            message='Short URL suffix can only contain lowercase alphabets, Uppercase alphabets and numbers',
        ),
    ])
    hits = models.IntegerField(default=0)


@dataclass
class UrlInputFields:
    url: str
