from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''Database model for users in the system'''
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    user_name = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name',]

    objects = CustomUserManager()

    def get_full_name(self):
        '''Retrieve full name of user'''
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.user_name

    def __str__(self):
        '''Return string representation of user'''
        return self.user_name

class Intern(models.Model):
    intern=models.OneToOneField(CustomUser, on_delete = models.CASCADE,related_name='user')

    def __str__(self):
        return f"{ self.intern.user_name}"



class UserProfile(models.Model):
    ROLES_TYPE_CHOICES = [
        ("SUPERVISOR",'SUPERVISOR'),
        ("INTERN",'INTERN'),
        ("None",'None'),
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name=_('userprofile'),
        primary_key=True
    )
    role = models.CharField(max_length=10, null=True, blank=True, choices=ROLES_TYPE_CHOICES, default=None)


    def __str__(self) -> str:
        return str(self.user.email)


    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class Attendance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    present=models.BooleanField(default=False)

    def __str__(self):
        return f"{ self.created_at}"


class Task(models.Model):
    task_name=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    start_date = models.DateTimeField(default=timezone.now)
    deadline=models.DateTimeField()
    completed=models.BooleanField(default=False)
    intern=models.ManyToManyField(Intern)

    class Meta:
        ordering = ["start_date"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{ self.task_name}"
    