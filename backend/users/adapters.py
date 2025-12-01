from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def clean_username(self, username):
        # Т.к. username нет — запрещаем allauth добавлять его
        return None

    def save_user(self, request, user, form, commit=True):
        # allauth создаёт юзера — мы должны сохранить phone,
        # иначе он попытается создать user без обязательного поля
        data = form.cleaned_data
        user.email = data.get("email")
        user.phone = data.get("phone")

        user.set_password(data.get("password1"))
        if commit:
            user.save()
        return user


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user

        # поля соцсети (VK, Yandex) — заполняем email если есть
        if not user.email:
            user.email = sociallogin.account.extra_data.get("email")

        # phone соцсети обычно не дают, ставим рандом
        if not user.phone:
            user.phone = f"vk_{sociallogin.account.uid}"

        user.is_active = True
        user.is_verified_email = True  # соцсети дают проверенный email
        user.save()

        return user


# CustomAccountAdapter.save_user — вызывается при обычной регистрации (forms). Нужно заполнить обязательные поля (phone) и сохранить.

# CustomSocialAccountAdapter.save_user — вызывается при первом входе через соцсеть. Часто соцсети дают email, тогда можно пометить is_verified_email = True.
