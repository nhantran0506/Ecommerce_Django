from typing import Any
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .enums import *

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extrafield):
        if not email:
            return
        
        email = self.normalize_email(email)
        user = self.model(email, **extrafield)
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_user(self, email = None, password = None, **extrafield):
        extrafield.setdefault("is_staff", False)
        extrafield.setdefault("is_superuser", False)
        return self._create_user(email, password, **extrafield)
    
    
    def create_superuser(self, email = None, password = None, **extrafield):
        extrafield.setdefault("is_staff", True)
        extrafield.setdefault("is_superuser", True)
        return self._create_user(email, password, **extrafield)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=False, unique=True, default='')
    name = models.CharField(max_length=255, blank=False, default='user')
    role = models.CharField(UserRoles.choices(), null = False, default=UserRoles.BUYER.value, max_length=15)
    date_of_birth = models.DateTimeField(blank=False,null=False)

    reset_code = models.CharField(max_length=10, null=True)
    reset_code_exp = models.DateTimeField(null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(default=timezone.now())

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User'