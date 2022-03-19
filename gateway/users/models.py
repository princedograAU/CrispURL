from uuid import uuid4

from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin

from commons.models import TimestampedModel


class UserManager(BaseUserManager):
    def create_user(self):
        user = self.model()
        user.save(using=self._db)
        return user


class User(TimestampedModel, PermissionsMixin):
    id = models.UUIDField(primary_key=True, null=False, db_index=True, editable=False, default=uuid4)

    objects = UserManager()
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    is_anonymous = False
    is_authenticated = True
    is_active = True

    def save(self, *args, **kwargs):
        self.full_clean()
        super(User, self).save(*args, **kwargs)
