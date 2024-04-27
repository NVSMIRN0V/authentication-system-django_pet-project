from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    # is_superuser больше не нужен
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    # Ненужные
    groups = None
    _password = None
    last_name = None
    last_login = None
    first_name = None
    date_joined = None
    user_permissions = None
   
    # Нужные
    is_active = True
    is_superuser = True
    email = models.EmailField("email address", blank=True)
    password = models.CharField("password", max_length=128)
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
    )

    # Ключевые поля
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"

    # UserManager
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        db_table = 'users'
