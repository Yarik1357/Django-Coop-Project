from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "role", "is_staff", "is_superuser")
    list_filter = ("role", "is_staff", "is_superuser", "is_active")
    
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Персональные данные", {"fields": ("first_name", "last_name")}),
        ("Роли и права", {"fields": ("role", "is_staff", "is_superuser", "is_active", "groups", "user_permissions")}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "role", "is_staff", "is_superuser", "is_active")}
        ),
    )
    
    search_fields = ("username", "email")
    ordering = ("username",)
