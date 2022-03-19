from django.db import models


class TimestampedModel(models.Model):
    # A timestamp representing when this object was created
    dt_created = models.DateTimeField(auto_now_add=True, null=False)

    # A timestamp representing when this object was last updated
    dt_last_changed = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True
        ordering = ['-dt_created', '-dt_last_changed']
