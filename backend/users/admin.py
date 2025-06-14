from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class ProfileLine(admin.TabularInline):
    model = Profile
    extra = 0


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ("email", "phone", "is_staff", "is_superuser", "has_profile")
    search_fields = ("email", "phone")
    ordering = ("email",)
    inlines = (ProfileLine,)
    fieldsets = (
        (None, {"fields": ("email", "phone", "password")}),
        (
            "Permissions",
            {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")},
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
