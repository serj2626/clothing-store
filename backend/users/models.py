from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone

from common.models import BaseDate, BaseID


class UserManager(BaseUserManager):
    """
    Менеджер пользователей
    """

    def create_user(self, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, phone, password, **extra_fields)


class User(BaseID, AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователя
    """

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    is_verified_email = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone"]

    def __str__(self):
        return (
            f'Администратор {self.email}'
            if self.is_staff
            else f'Пользователь {self.email}'
        )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


# class EmailVerification(models.Model):
#     code = models.UUIDField(unique=True)
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     expiration = models.DateTimeField()

#     def __str__(self):
#         return f"EmailVerification object for {self.user.email}"

# def send_verification_email(self):
#     link = reverse(
#         "users:email_verification",
#         kwargs={"email": self.user.email, "code": self.code},
#     )
#     verification_link = f"{settings.DOMAIN_NAME}{link}"
#     subject = f"Подверждение учетной записи для {self.user.username}"
#     message = (
#         "Для подверждения учетной записи для {} перейдите по ссылке: {}".format(
#             self.user.email, verification_link
#         )
#     )
#     send_mail(
#         subject=subject,
#         message=message,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[self.user.email],
#         fail_silently=False,
#     )

# def is_expired(self):
#     return True if now() >= self.expiration else False


class Profile(BaseID, BaseDate):
    """
    Модель профиля
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("Имя", max_length=50, null=True, blank=True)
    last_name = models.CharField(
        "Фамилия", max_length=50, null=True, blank=True
    )
    city = models.CharField("Город", max_length=50, null=True, blank=True)
    address = models.CharField("Адрес", max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f'Профиль "{self.user.email}"'
