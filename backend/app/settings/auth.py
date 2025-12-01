from datetime import timedelta

ACCOUNT_EMAIL_REQUIRED = True
# — e-mail обязателен при регистрации. Allauth будет требовать поле email.

ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# — 'none' | 'optional' | 'mandatory'
# mandatory — пользователь должен подтвердить e-mail перед входом (или до получения статуса verified).

ACCOUNT_AUTHENTICATION_METHOD = "email"
# — 'username', 'email', 'username_email'
# мы используем e-mail как логин (у тебя USERNAME_FIELD="email").

ACCOUNT_USERNAME_REQUIRED = False
# — отключаем username, т.к. в модели его нет/не используем.

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# — явное указание allauth, что field username отсутствует.

LOGIN_REDIRECT_URL = "/"
# — куда перенаправлять после успешного логина (если используется HTML-редирект flow).
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ACCOUNT_ADAPTER = "users.adapters.CustomAccountAdapter"
SOCIALACCOUNT_ADAPTER = "users.adapters.CustomSocialAccountAdapter"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # dev
# для продакшна ставим SMTP: SMTP backend/Yandex/Gmail
DEFAULT_FROM_EMAIL = "no-reply@yourdomain.com"

ACCOUNT_DEFAULT_HTTP_PROTOCOL = (
    "https"  # production (для генерации ссылок в письмах)
)
# Иногда нужен BACKEND_HOST или DOMAIN — чтобы письма и redirect формировали правильные URL.

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_COOKIE": "access_token_store",
    "AUTH_COOKIE_REFRESH": "refresh_token_store",
    "AUTH_COOKIE_SECURE": False,  # True на проде
    "AUTH_COOKIE_HTTP_ONLY": True,
    "AUTH_COOKIE_PATH": "/",
    "AUTH_COOKIE_SAMESITE": "Lax",
}
