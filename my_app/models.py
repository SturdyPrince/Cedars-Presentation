from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(username=username, first_name=first_name, last_name=last_name, email=self.normalize_email(email))
        user.set_password(password)
        return user
    
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=50, verbose_name="Email address", unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
    

