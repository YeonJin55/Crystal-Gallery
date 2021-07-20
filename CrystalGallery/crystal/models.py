from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField(default=timezone.now(), null=True)
    username = models.CharField(max_length=30, unique=True, null=True)
    nickname = models.CharField(max_length=30, unique=True, null=True)
    coin = models.IntegerField(default=9999)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Listing(models.Model):
    DEFAULT_USER = 1
    name = models.CharField(max_length = 100, blank = False)
    initial = models.DecimalField(max_digits = 10, decimal_places = 2)
    user = models.ForeignKey(User, blank = False, on_delete = models.CASCADE, default = DEFAULT_USER)
    image = models.ImageField(upload_to='images/')
    created = models.DateField(auto_now_add = True)
    explain = models.TextField(default = '')

    def __str__(self):
        return f"{self.name} - starts at ${self.initial}"

    # used to test in test.py
    def is_valid_listing(self):
        return len(self.name) > 0 and self.initial > 0


class Bid(models.Model):
    user = models.ForeignKey(User, blank = False, on_delete = models.CASCADE)
    listing = models.ForeignKey(Listing, blank = False, on_delete = models.CASCADE)
    highest_bid = models.DecimalField(max_digits = 10, decimal_places = 2)
    added = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"${self.highest_bid} - {self.user} on {self.listing.name}"

