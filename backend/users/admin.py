from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, User


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for'''

    list_display = (
        'user',
        'first_name',
        'last_name',
    )


class ProfileLine(admin.TabularInline):
    model = Profile
    extra = 0


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "phone",
        "is_staff",
        "is_superuser",
        "has_profile",
    )
    # list_display = ("email", "phone", "is_staff", "is_superuser", )
    search_fields = ("email", "phone")
    ordering = ("email",)
    inlines = (ProfileLine,)
    fieldsets = (
        (None, {"fields": ("email", "phone", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "phone",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    def has_profile(self, obj):
        return hasattr(obj, "profile")

    has_profile.boolean = True
    has_profile.short_description = "Профиль есть?"
