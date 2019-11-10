from django.db import models

# Create your models here.
from django.core.validators import RegexValidator

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

AUTHORISED_PERSONNEL = [
    ('Medical Doctor', 'Doctor'),
    ('Nurse', 'Nurse'),
    ('Secretary', 'Secretary'),
    ('Department of Health Rep', 'Health Officer')
]

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username, email, password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    username = models.CharField(
                    max_length=255,
                    validators = [
                        RegexValidator(regex = USERNAME_REGEX,
                                message = 'Username must be alphanumeric or contain numbers',
                                code = 'invalid username'

                        )],
                     unique = True
                )

    email = models.EmailField(
        max_length=255,
        unique= True,
        verbose_name='email address'
    )

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return '{0} With Email {1}' .format(self.username, self.email)

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'"
        # Simplest possible answer: Yes, always
        return True


    class Meta:
        verbose_name_plural = "Administrators"
        ordering = ("-username",)


class AuthorisedUsers(AbstractBaseUser):
    username = models.CharField(
                    max_length=255,
                    validators = [
                        RegexValidator(regex = USERNAME_REGEX,
                                message = 'Username must be alphanumeric or contain numbers',
                                code = 'invalid username'

                        )],
                     unique = True
                )

    email = models.EmailField(
        max_length=255,
        unique= True,
        verbose_name='email address'
    )

    position = models.CharField(
        max_length=70,
        choices=AUTHORISED_PERSONNEL,
        verbose_name = 'Level of Access'
    )

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return '{0} With Email {1}' .format(self.username, self.email)

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'"
        # Simplest possible answer: Yes, always
        return True


    class Meta:
        verbose_name_plural = "Authorised Users"
        ordering = ("-username",)
