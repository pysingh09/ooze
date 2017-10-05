from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    #method which created user in accounts.user table
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)
    #method which creates super user in db
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)

class User(AbstractBaseUser):

    #custom user model which has email as primary key
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    is_active = models.BooleanField(default=False)
    last_password_reset_datetime = models.DateTimeField(null = True)
    last_signout_datetime = models.DateTimeField(default = datetime.now, null = True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, null = True, blank=True)
    last_name = models.CharField(max_length=30, null = True, blank=True)
    user_name = models.CharField(max_length=30, null = True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_first_name(self):
        # For this case we return email. Could also be User.first_name User.last_name if you have these fields
        return self.first_name

    def get_last_name(self):
        # For this case we return email. Could also be User.first_name if you have this field
        return self.last_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        # Handle whether the user has a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # Handle whether the user has permissions to view the app `app_label`?"
        return True

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name


