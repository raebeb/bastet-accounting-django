from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    current_sign_in_ip = models.GenericIPAddressField(null=True, blank=True)
    last_sign_in_ip = models.GenericIPAddressField(null=True, blank=True)
    #TODO: make this a foreign key to a team model
    current_team = models.CharField('current team', max_length=50)

    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='accounting_user_permissions')


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        pass
