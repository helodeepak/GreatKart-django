from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, user_name, email, password=None):
        if not email:
            raise ValueError('User must have email address')
        if not user_name:
            raise ValueError('user must have user name')

        user = self.model(
            email = self.normalize_email(email),
            user_name = user_name,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, first_name, last_name, user_name, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            user_name = user_name,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user


class Account(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email     = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)

    # required field
    date_joining = models.DateTimeField(auto_now_add=True)
    last_login  = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # set default user name is email

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects = MyAccountManager()

    def _str_(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True