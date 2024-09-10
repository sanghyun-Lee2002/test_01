from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, name, nickname, birthday, password=None, **extra_fields):
        if not username:
            raise ValueError('Username is required')
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            name=name,
            nickname=nickname,
            birthday=birthday,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, nickname, birthday, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, name, nickname, birthday, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=30)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'nickname', 'birthday']

    def __str__(self):
        return self.username
   
    # first_name = None
    # last_name = None
    # email = models.EmailField(unique=True)
    # name = models.CharField(max_length=15)
    # nickname = models.CharField(max_length=20)
    # birthday = models.DateField()

    # gender = models.CharField(blank=True, max_length=2)
    # memo = models.TextField(blank=True)

    

# Create your models here.dsde