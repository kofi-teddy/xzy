from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField('Emailaddress', unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    send_email_for_downtime = models.BooleanField(default=True)
    send_email_for_issues = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    def has_module_perms(self, app_label):
        return f'{self.first_name}, {self.last_name}'

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    

def save(self, *args, **kwargs):
    self.email = self.email.lower()
    return super(User, self).save(*args, **kwargs) 