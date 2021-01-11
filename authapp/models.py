from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', blank=True)
    age = models.PositiveIntegerField(blank=True, null=True)


