from datetime import datetime

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class CustomUserManager(BaseUserManager):
    
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The given email  must be set')
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            date_joined=datetime.now(), 
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField('Email address', unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    send_email_for_downtime = models.BooleanField(default=True)
    send_email_for_issues = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
    
    object = CustomUserManager()
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        return super(User, self).save(*args, **kwargs) 


