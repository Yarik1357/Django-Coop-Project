from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "admin", "Администратор"
        MODERATOR = "moderator", "Модератор"
        USER = "user", "Користувач"

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.USER
    )

    def is_admin(self):
        return self.role == self.Roles.ADMIN

    def is_moderator(self):
        return self.role == self.Roles.MODERATOR