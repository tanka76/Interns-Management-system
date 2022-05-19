from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,UserProfile,Task,Intern,Attendance
from django.forms.widgets import Textarea

admin.site.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['role','user']

admin.site.register(Intern)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id','user','present','created_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','task_name','description','start_date','deadline','completed']




class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "id",
        "email",
        "user_name",
        "first_name",
        "last_name",
        "date_joined",
        "is_verified",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "user_name",
        "is_verified",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                    "last_name",
                    "password",
                  
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_verified",
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "date_joined",
                    "is_verified",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
